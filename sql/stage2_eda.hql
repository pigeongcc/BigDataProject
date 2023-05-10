USE project;


-- query 1
-- users table is useless as it contains false vote_count value
INSERT OVERWRITE LOCAL DIRECTORY 'output/eda/q1'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'

SELECT user_id, COUNT(*) AS vote_count
FROM ratings_opt
WHERE user_id = 'deathproof'
GROUP BY user_id;


-- query 2
-- users with low real vote_count value
INSERT OVERWRITE LOCAL DIRECTORY 'output/eda/q2'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'

SELECT movie_id, COUNT(*) AS vote_count
FROM ratings_opt
GROUP BY movie_id
SORT BY vote_count ASC;


-- query 3
-- movies with low real vote_count value
INSERT OVERWRITE LOCAL DIRECTORY 'output/eda/q3'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'

SELECT user_id, COUNT(*) AS vote_count
FROM ratings_opt
GROUP BY user_id
SORT BY vote_count ASC;


-- query 4
-- Cast genres column from string to array<string>
DROP TABLE IF EXISTS dummy_genres;
CREATE TABLE dummy_genres(genres_arr ARRAY<STRING>);

WITH genres_column AS
(SELECT genres FROM movies_opt),
genres_array AS 
(SELECT split(regexp_extract(genres, '^\\["(.*)\\"]$',1),'","')
FROM genres_column)
INSERT INTO dummy_genres SELECT * FROM genres_array;


INSERT OVERWRITE LOCAL DIRECTORY 'output/eda/q4'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'

SELECT genre, COUNT(*) genre_ctr
FROM dummy_genres
LATERAL VIEW explode(genres_arr) dummy_genres AS genre
GROUP BY genre
SORT BY genre_ctr DESC;


-- query 5
-- popularity distribution
INSERT OVERWRITE LOCAL DIRECTORY 'output/eda/q5'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'

SELECT movie_id, popularity
FROM movies_opt
SORT BY popularity DESC;