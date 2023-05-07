-- create a database project
DROP DATABASE IF EXISTS project;
CREATE DATABASE project;


--switch to the database project
\c project;


-- add tables 

/*
CREATE TABLE users (
	_id TEXT NOT NULL,
	display_name TEXT,
	num_ratings_pages INTEGER,
	num_reviews INTEGER,
	username TEXT NOT NULL PRIMARY KEY
); */

CREATE TABLE movies (
	_id TEXT NOT NULL,
	genres TEXT,
	--_image_url TEXT,
	imdb_id TEXT,
	--_imdb_link TEXT,
	movie_id TEXT NOT NULL PRIMARY KEY,
	movie_title TEXT,
	original_language TEXT,
	overview TEXT,
	popularity REAL,
	temp_production_countries TEXT,
	release_date DATE,
	runtime REAL,
	temp_spoken_languages TEXT,
	--_tmdb_id TEXT,
	--_tmdb_link TEXT,
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


-- load data from csv files
SET datestyle TO iso, ymd;

--\COPY users FROM 'data/users_export.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER, NULL '');
\COPY movies FROM 'data/movie_data_pd.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER, NULL '');
\COPY ratings FROM 'data/ratings_export_pd.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER, NULL '');


-- add constraints

/*
ALTER TABLE ratings
ADD CONSTRAINT fk_user_username_userid
FOREIGN KEY (user_id)
REFERENCES users(username); */

ALTER TABLE ratings
ADD CONSTRAINT fk_movie_movieid_movieid
FOREIGN KEY (movie_id)
REFERENCES movies(movie_id);