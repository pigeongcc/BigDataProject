#!/bin/bash

# create folder in hfds for .avsc files from avro
hdfs dfs -mkdir /project/avsc

# move .avsc files into hdfs
hdfs dfs -put output/avsc/movies.avsc /project/avsc
hdfs dfs -put output/avsc/ratings.avsc /project/avsc
# hdfs dfs -put ../avsc/users.avsc /project/avsc

# execute HiveQL script
hive -f ./sql/stage2.hql


# build csv files for EDA part
# query 1
echo "genres,count" > output/eda/q1/q1.csv
cat output/eda/q1/* >> output/q1.csv

# query 2