#!/bin/bash

# echo a blank line for the sake of output readability
echo

# run the sql script to build a relational database
psql -U postgres -d project -f stage1/db.sql

# some operation on the resulted DB
echo "
\c project;
SELECT * FROM ratings LIMIT 3;
" | psql -U postgres