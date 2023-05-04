#!/bin/bash

# echo a blank line for the sake of output readability
echo

echo "

-- create a database project
DROP DATABASE IF EXISTS project;
CREATE DATABASE project;


--switch to the database project
\c project;


-- add tables 

CREATE TABLE users (
	_id TEXT NOT NULL,
	display_name TEXT,
	num_ratings_pages INTEGER,
	num_reviews INTEGER,
	username TEXT NOT NULL PRIMARY KEY
);

CREATE TABLE movies (
	_id TEXT NOT NULL,
	genres TEXT [],
	_image_url TEXT,
	imdb_id TEXT,
	_imdb_link TEXT,
	movie_id TEXT NOT NULL PRIMARY KEY,
	movie_title TEXT,
	original_language TEXT,
	overview TEXT,
	popularity REAL,
	temp_production_countries TEXT,
	release_date DATE,
	runtime REAL,
	temp_spoken_languages TEXT,
	_tmdb_id TEXT,
	_tmdb_link TEXT,
	vote_average REAL,
	vote_count REAL,
	year_released REAL
);
-- runtime: convert 0 and null to NULL

CREATE TABLE ratings (
	id TEXT NOT NULL PRIMARY KEY,
	movie_id TEXT NOT NULL,
	rating_val INTEGER NOT NULL,
	user_id TEXT NOT NULL
);


-- add constraints

ALTER TABLE ratings
ADD CONSTRAINT fk_user_username_userid
FOREIGN KEY (user_id)
REFERENCES users(username);

ALTER TABLE ratings
ADD CONSTRAINT fk_movie_movieid_movieid
FOREIGN KEY (movie_id)
REFERENCES movies(movie_id);


-- load data from csv files
SET datestyle TO iso, ymd;

\COPY users FROM 'data/users_export.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER, NULL '');
\COPY movies FROM 'data/movie_data.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER, NULL 'null');
--\COPY users FROM 'data/users_export.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER, NULL '');

SELECT *
FROM movies
LIMIT 10;



CREATE TABLE mytype (id uuid, amount numeric(13,4));  INSERT INTO mytype VALUES   ('0d6311cc-0d74-4a32-8cf9-87835651e1ee', 25)  ,('6449fb3b-844e-440e-8973-31eb6bbefc81', 10);  SELECT ARRAY(SELECT m FROM mytype m);


" | psql -U postgres






