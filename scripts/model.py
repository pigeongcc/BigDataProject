import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .appName("BDT Project")\
        .config("spark.sql.catalogImplementation","hive")\
        .config("hive.metastore.uris", "thrift://sandbox-hdp.hortonworks.com:9083")\
        .config("spark.sql.avro.compression.codec", "snappy")\
        .enableHiveSupport()\
        .getOrCreate()


# print(spark.catalog.listDatabases())

# print(spark.catalog.listTables("project"))

movies = spark.read.format("avro").table('project.movies')
movies.createOrReplaceTempView('movies')
movies.printSchema()

ratings = spark.read.format("avro").table("project.ratings")
ratings.createOrReplaceGlobalTempView('ratings')
ratings.printSchema()

# spark.sql("SELECT * FROM movies limit 10").show()