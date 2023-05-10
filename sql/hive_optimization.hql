-- setup partitioning and bucketing
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

SET hive.enforce.bucketing=true;

-- create optimized ratings table
DROP TABLE IF EXISTS ratings_opt;
CREATE EXTERNAL TABLE ratings_opt(
    movie_id STRING,
    user_id STRING
) 
PARTITIONED BY (rating_val INT)
CLUSTERED BY (user_id) INTO 300 BUCKETS
STORED AS AVRO LOCATION '/project/ratings_opt'
TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- create optimized movies table
DROP TABLE IF EXISTS movies_opt;
CREATE EXTERNAL TABLE movies_opt(
	genres STRING,
	movie_id STRING,
	popularity FLOAT,
	release_date DATE
)
PARTITIONED BY (year_released FLOAT)
CLUSTERED BY (movie_id) INTO 100 BUCKETS
STORED AS AVRO LOCATION '/project/movies_opt'
TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- insert the data from unpartitioned tables
INSERT INTO ratings_opt SELECT * FROM ratings;
INSERT INTO movies_opt SELECT * FROM movies;
