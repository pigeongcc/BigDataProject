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
