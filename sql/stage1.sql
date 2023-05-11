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
); 
*/

CREATE TABLE movies (
	genres TEXT,
	movie_id TEXT NOT NULL PRIMARY KEY,
	popularity REAL,
	release_date DATE,
	year_released INTEGER
);

CREATE TABLE ratings (
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