-- create database
DROP DATABASE IF EXISTS project CASCADE;
CREATE DATABASE project;
USE project;

-- Since the data files are compressed in Snappy codec, 
-- we need to set some configurations for loading the data from HDFS as follows:
SET mapreduce.map.output.compress = true;
SET mapreduce.map.output.compress.codec = org.apache.hadoop.io.compress.SnappyCodec;

-- Create tables
--CREATE EXTERNAL TABLE users STORED AS AVRO LOCATION '/project/users' TBLPROPERTIES ('avro.schema.url'='/project/avsc/users.avsc');
CREATE EXTERNAL TABLE ratings STORED AS AVRO LOCATION '/project/ratings' TBLPROPERTIES ('avro.schema.url'='/project/avsc/ratings.avsc');
CREATE EXTERNAL TABLE movies STORED AS AVRO LOCATION '/project/movies' TBLPROPERTIES ('avro.schema.url'='/project/avsc/movies.avsc');