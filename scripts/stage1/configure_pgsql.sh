# edit PostgreSQL config
sed -i '1s/^/local all all trust\n/' /var/lib/pgsql/data/pg_hba.conf
sed -i '1s/^/host all postgres 127.0.0.1\/32 trust\n/' /var/lib/pgsql/data/pg_hba.conf
# LINE='local all all trust host all postgres 127.0.0.1/32 trust'
# FILE='/var/lib/pgsql/data/pg_hba.conf'
# grep -xqF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"

# restart PostgreSQL server
systemctl restart postgresql

# download (if not exists) and install the JDBC driver
wget -nc https://jdbc.postgresql.org/download/postgresql-42.6.0.jar --no-check-certificate
cp  postgresql-42.6.0.jar /usr/hdp/current/sqoop-client/lib/