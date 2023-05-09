#!/bin/bash

# create folder in hfds for .avsc files from avro
hdfs dfs -rm -r /project/avsc   # remove it if exists
hdfs dfs -mkdir /project/avsc

# move .avsc files into hdfs
hdfs dfs -put output/avsc/movies.avsc /project/avsc
hdfs dfs -put output/avsc/ratings.avsc /project/avsc
# hdfs dfs -put ../avsc/users.avsc /project/avsc

# execute HiveQL script
hive -f ./sql/stage2.hql

# run EDA
hive -f ./sql/stage2_eda.hql

# build csv files for EDA part
# query 1
echo -e "user_id\tvote_count" > output/eda/q1.csv
cat output/eda/q1/* >> output/eda/q1.csv

# query 2
echo -e "movie_id\tvote_count" > output/eda/q2.csv
cat output/eda/q2/* >> output/eda/q2.csv

# query 3
echo -e "user_id\tvote_count" > output/eda/q3.csv
cat output/eda/q3/* >> output/eda/q3.csv

# query 4
echo -e "genre\tcount" > output/eda/q4.csv
cat output/eda/q4/* >> output/eda/q4.csv

# query 4
echo -e "movie_id\tpopularity" > output/eda/q5.csv
cat output/eda/q5/* >> output/eda/q5.csv