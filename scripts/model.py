import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.ml.feature import StringIndexer
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import ParamGridBuilder
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.feature import IndexToString
from pyspark.sql.types import StructType, StructField, StringType

SEED = 42


spark = SparkSession.builder\
        .appName("BDT Project")\
        .config("spark.sql.catalogImplementation", "hive")\
        .config("hive.metastore.uris", "thrift://sandbox-hdp.hortonworks.com:9083")\
        .config("spark.sql.avro.compression.codec", "snappy")\
        .enableHiveSupport()\
        .getOrCreate()


movies = spark.read.format("avro").table('project.movies')
movies.createOrReplaceTempView('movies')
movies.printSchema()

ratings = spark.read.format("avro").table("project.ratings")
ratings.createOrReplaceGlobalTempView('ratings')
ratings.printSchema()

ratings.show(5)
ratings = ratings.drop('id')

movie_indexer = StringIndexer(inputCol="movie_id", outputCol="movie_id_enc")
movie_indexer = movie_indexer.fit(ratings)
ratings = movie_indexer.transform(ratings)
ratings = ratings.drop("movie_id")
ratings.show(3)

user_indexer = StringIndexer(inputCol="user_id", outputCol="user_id_enc")
user_indexer = user_indexer.fit(ratings)
ratings = user_indexer.transform(ratings)
ratings = ratings.drop("user_id")
ratings.show(3)


(training, test) = ratings.randomSplit([0.7, 0.3], seed=SEED)

als = ALS(
    maxIter=10, 
    regParam=0.1, 
    userCol="user_id_enc",
    itemCol="movie_id_enc", 
    ratingCol="rating_val", 
    coldStartStrategy="drop",
    seed=SEED,
    nonnegative=True
)
          
# model = als.fit(training)


param_grid = ParamGridBuilder().addGrid(als.regParam, [.05, 1]).build()
# .addGrid(als.rank, [5, 40, 80, 120])
# .addGrid(als.maxIter, [5, 100, 250, 500])
# .addGrid(als.regParam, [.05, .1, 1.5])
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating_val", predictionCol="prediction")
cv = CrossValidator(estimator=als, estimatorParamMaps=param_grid, evaluator=evaluator, numFolds=2)

model = cv.fit(training)
best_model = model.bestModel
best_model.save('models/best_als')
predictions = best_model.transform(test)
rmse = evaluator.evaluate(predictions)

print("**Best Model**")
print("RMSE =", rmse)
print(" Rank:", best_model.rank)
# print(" MaxIter:", best_model._java_obj.parent().getMaxIter())
# print(" RegParam:", best_model._java_obj.parent().getRegParam())


def suggest_for_user(user_name, limit=5):
    data = [(user_name,)]
    schema = StructType([StructField("user_id", StringType(), True)])
    df = spark.createDataFrame(data=data, schema=schema)
    
    df = user_indexer.transform(df)
    user = df.collect()[0].user_id_enc

    user_prods = ratings.select("movie_id_enc").distinct() \
        .join(ratings.filter("user_id_enc=" + \
        str(user)).select("user_id_enc").distinct(), how="full")
    user_prods.summary().show()

    user_prods_res = model.transform(user_prods)
    user_prods_res.show()

    top_products = user_prods_res.sort(F.desc("prediction")).limit(limit).select("movie_id_enc")
    movie_inverter = IndexToString(
        inputCol="movie_id_enc", 
        outputCol="movie", 
        labels=movie_indexer.labels
    )
    itd = movie_inverter.transform(top_products)

    itd = itd.drop("movie_id_enc")
    print('Recommended films for', user_name)
    itd.show()

suggest_for_user('hafilova')