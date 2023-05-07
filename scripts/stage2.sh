#!/bin/bash

# create folder in hfds for .avsc files from avro
hdfs dfs -mkdir /project/avsc

# move .avsc files into hdfs
hdfs dfs -put ../avsc/movies.avsc /project/avsc
hdfs dfs -put ../avsc/ratings.avsc /project/avsc
# hdfs dfs -put ../avsc/users.avsc /project/avsc

# execute HiveQL script
hive -f ./sql/stage2.hql