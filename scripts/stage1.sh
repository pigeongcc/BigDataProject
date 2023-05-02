#!/bin/bash

echo

# drop the databases if exist
psql -U postgres -c 'DROP DATABASE IF EXISTS project;'

# create a database project
psql -U postgres -c 'CREATE DATABASE project;'

