#!/bin/bash

# echo a blank line for the sake of output readability
echo

# configure the PostgreSQL server, install JDBC driver
bash scripts/stage1/configure_pgsql.sh

# run the sql script to build a relational database
#psql -U postgres -d project -f ../sql/stage1.sql
psql -U postgres -f ./sql/stage1.sql

# some operation on the resulted DB
echo "
\c project;
SELECT * FROM ratings LIMIT 3;
" | psql -U postgres

# deletes compressed avro files on db from hdfs
hdfs dfs -rm -r /project

# creates compressed avro files
sqoop import-all-tables \
    -Dmapreduce.job.user.classpath.first=true \
    --connect jdbc:postgresql://localhost/project \
    --username postgres \
    --warehouse-dir /project \
    --as-avrodatafile \
    --compression-codec=snappy \
    --outdir output/avsc \
    --m 1