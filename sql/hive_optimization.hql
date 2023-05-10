USE project;

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
CLUSTERED BY (user_id) INTO 10 BUCKETS
STORED AS AVRO LOCATION '/project/ratings_opt'
TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- create optimized movies table
DROP TABLE IF EXISTS movies_opt;
CREATE EXTERNAL TABLE movies_opt(
	genres STRING,
	movie_id STRING,
	popularity FLOAT,
	release_date STRING
)
PARTITIONED BY (year_released FLOAT)
CLUSTERED BY (movie_id) INTO 5 BUCKETS
STORED AS AVRO LOCATION '/project/movies_opt'
TBLPROPERTIES ('AVRO.COMPRESS'='SNAPPY');

-- insert the data from unpartitioned tables
INSERT INTO ratings_opt PARTITION (rating_val) SELECT movie_id, rating_val, user_id FROM ratings;
INSERT INTO movies_opt PARTITION (year_released) SELECT genres, movie_id, popularity, release_date, year_released FROM movies;
