#!/bin/bash

# echo a blank line for the sake of output readability
echo

# run the sql script to build a relational database
#psql -U postgres -d project -f ../sql/stage1.sql
psql -U postgres -f ./sql/stage1.sql

# some operation on the resulted DB
echo "
\c project;
SELECT * FROM ratings LIMIT 3;
" | psql -U postgres

# edit PostgreSQL config
# sed -i '1s/^/<local all all trust> /' /var/lib/pgsql/data/pg_hba.conf
LINE='local all all trust'
FILE='/var/lib/pgsql/data/pg_hba.conf'
grep -xqF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"

# restart PostgreSQL server
systemctl restart postgresql

# download (if not exists) and install the JDBC driver
wget -nc https://jdbc.postgresql.org/download/postgresql-42.6.0.jar --no-check-certificate
cp  postgresql-42.6.0.jar /usr/hdp/current/sqoop-client/lib/