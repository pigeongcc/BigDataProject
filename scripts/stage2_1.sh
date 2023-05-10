#!/bin/bash
echo

# create folder in hfds for .avsc files from avro
hdfs dfs -rm -r /project/avsc   # remove it if exists
hdfs dfs -mkdir /project/avsc

# move .avsc files into hdfs
hdfs dfs -put output/avsc/movies.avsc /project/avsc
hdfs dfs -put output/avsc/ratings.avsc /project/avsc
# hdfs dfs -put ../avsc/users.avsc /project/avsc

# execute HiveQL scripts
echo -e "\n~ ~ ~ Running stage2.hql\n"
hive -f ./sql/stage2.hql