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

ratings = spark.read.format("avro").table("project.ratings")
ratings.createOrReplaceGlobalTempView('ratings')
ratings.printSchema()

movie_indexer = StringIndexer(inputCol="movie_id", outputCol="movie_id_enc")
movie_indexer = movie_indexer.fit(ratings)
ratings = movie_indexer.transform(ratings)
ratings = ratings.drop("movie_id")
ratings.show(3)

movie_indexer.save('models/best_als')