INSERT OVERWRITE LOCAL DIRECTORY 'output/eda'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT dname, COUNT(*) 
FROM departments AS d JOIN employees AS e
ON d.deptno = e.deptno
GROUP BY dname 
ORDER BY d.dname;