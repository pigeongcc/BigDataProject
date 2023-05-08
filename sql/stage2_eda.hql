USE project;


-- query 1
INSERT OVERWRITE LOCAL DIRECTORY 'output/eda/q1'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'

SELECT genres, COUNT(*) as ctr
FROM movies
GROUP BY genres
SORT BY ctr DESC
LIMIT 15;


-- query 2
-- Cast genres column from string to array<string>
DROP TABLE IF EXISTS dummy_genres;
CREATE TABLE dummy_genres(genres_arr ARRAY<STRING>);

WITH genres_column AS
(SELECT genres FROM movies),
genres_array AS 
(SELECT split(regexp_extract(genres, '^\\["(.*)\\"]$',1),'","')
FROM genres_column)
INSERT INTO dummy_genres SELECT * FROM genres_array;


INSERT OVERWRITE LOCAL DIRECTORY 'output/eda/q2'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'

SELECT genre, COUNT(*) genre_ctr
FROM dummy_genres
LATERAL VIEW explode(genres_arr) dummy_genres AS genre
GROUP BY genre
SORT BY genre_ctr ASC;