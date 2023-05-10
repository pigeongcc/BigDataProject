echo -e "\n~ ~ ~ Running hive_optimization.hql\n"
hive -f ./sql/hive_optimization.hql

# run EDA
echo -e "\n~ ~ ~ Running stage2_eda.hql\n"
hive -f ./sql/stage2_eda.hql

# build csv files for EDA part
# query 1
rm output/eda/q1.csv
echo -e "user_id\tvote_count" > output/eda/q1.csv
cat output/eda/q1/* >> output/eda/q1.csv

# query 2
rm output/eda/q2.csv
echo -e "movie_id\tvote_count" > output/eda/q2.csv
cat output/eda/q2/* >> output/eda/q2.csv

# query 3
rm output/eda/q3.csv
echo -e "user_id\tvote_count" > output/eda/q3.csv
cat output/eda/q3/* >> output/eda/q3.csv

# query 4
rm output/eda/q4.csv
echo -e "genre\tcount" > output/eda/q4.csv
cat output/eda/q4/* >> output/eda/q4.csv

# query 5
rm output/eda/q5.csv
echo -e "movie_id\tpopularity" > output/eda/q5.csv
cat output/eda/q5/* >> output/eda/q5.csv


echo -e "\n~ ~ ~ Finished stage 2!"