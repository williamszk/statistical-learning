-- how to start mysql?
-- we are using a windows machine

-- in here we already have mysql installed

-- start mysql shell 
mysqlsh -u william
-- the password for the local mysql
mNpL9UwjEPFxTpGjRdnvDbAvrqvVGNxs48LAEWAu
yes
-- change to sql terminal
\sql


SHOW DATABASES;

-- This video:
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8410308#overview


-- How to run an entire .sql file from the mysqlsh?
-- https://sebhastian.com/mysql-running-sql-file/
source ./udemy-mysql-for-analytics/220906/employees.sql;
-- it appears that this works but it does not

-- let's try to run without entering the mysqlsh
-- mysqlsh -u root -p employees < udemy-mysql-for-analytics/220906/employees.sql
-- bQ53EM3WnKLNzEcEZTK7m7rU9MVEQXDU7yMVZUNM
-- problem with using william user and root user
-- didn't work

-- I tried selecting the whole employees.sql and then sending it to the 
-- terminal running mysqlsh
-- this took to long
-- let's try another alternative

USE employees;
SHOW TABLES;

USE sales;
SHOW TABLES;

DESCRIBE employees;

-- Delete database
DROP DATABASE IF EXISTS employees;
SHOW DATABASES;

-- this solution here works <<<<<<<<<<<<<<<<<<<<<<
-- https://stackoverflow.com/a/50526916/8782077
-- mysqlsh -h localhost -u mixtape-dating -p -f setup.sql --sql
-- we could try this one:
mysqlsh -h localhost -u william -p -f employees.sql --sql
-- the suggestion of the other article didn't work
mNpL9UwjEPFxTpGjRdnvDbAvrqvVGNxs48LAEWAu
yes


-- enter the mysqlsh
mysqlsh -u william
mNpL9UwjEPFxTpGjRdnvDbAvrqvVGNxs48LAEWAu
yes
\sql

SHOW DATABASES;
USE employees;

SHOW TABLES;
-- It looks like it worked
--  MySQL  localhost:33060+ ssl  employees  SQL > SHOW TABLES;
-- +----------------------+
-- | Tables_in_employees  |
-- +----------------------+
-- | current_dept_emp     |
-- | departments          |
-- | dept_emp             |
-- | dept_emp_latest_date |
-- | dept_manager         |
-- | employees            |
-- | salaries             |
-- | titles               |
-- +----------------------+
-- 8 rows in set (0.0021 sec)

-- how to count the number of lines in table?
-- https://www.navicat.com/en/company/aboutus/blog/695-getting-row-counts-in-mysql-part-1#:~:text=Counting%20all%20of%20the%20Rows,returned%20by%20a%20SELECT%20statement.
SELECT COUNT(*) FROM employees;
-- +----------+
-- | COUNT(*) |
-- +----------+
-- |   300024 |
-- +----------+
-- 1 row in set (14.2209 sec)

-- this should be 499,000
-- why there is only 300024?
-- maybe there are some employees that are not in the database anymore


SELECT COUNT(*) FROM departments;
-- +----------+
-- | COUNT(*) |
-- +----------+
-- |        9 |
-- +----------+
-- 1 row in set (0.0099 sec)

-- ============================================================================
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8344762#overview

DESCRIBE employees;
--  MySQL  localhost:33060+ ssl  employees  SQL > DESCRIBE employees;
-- +------------+---------------+------+-----+---------+-------+     
-- | Field      | Type          | Null | Key | Default | Extra |     
-- +------------+---------------+------+-----+---------+-------+
-- | emp_no     | int           | NO   | PRI | NULL    |       |
-- | birth_date | date          | NO   |     | NULL    |       |
-- | first_name | varchar(14)   | NO   |     | NULL    |       |
-- | last_name  | varchar(16)   | NO   |     | NULL    |       |
-- | gender     | enum('M','F') | NO   |     | NULL    |       |
-- | hire_date  | date          | NO   |     | NULL    |       |
-- +------------+---------------+------+-----+---------+-------+
-- 6 rows in set (0.0091 sec)

SELECT first_name
    , last_name
FROM employees;
-- +----------------+------------------+
-- | first_name     | last_name        |
-- +----------------+------------------+
-- | Lene           | Ariola           |
-- | Zhenhua        | Sridhar          |
-- | Angel          | Malabarba        |
-- | Yinghua        | Kropf            |
-- | Ugo            | Salverda         |
-- | Shounak        | Seghrouchni      |
-- | Kazuhira       | Weedman          |
-- +----------------+------------------+
-- 300024 rows in set (0.0021 sec)


SELECT first_name
    , last_name
FROM employees
LIMIT 10
;
-- +------------+-----------+
-- | first_name | last_name |
-- +------------+-----------+
-- | Georgi     | Facello   |
-- | Bezalel    | Simmel    |
-- | Parto      | Bamford   |
-- | Chirstian  | Koblick   |
-- | Kyoichi    | Maliniak  |
-- | Anneke     | Preusig   |
-- | Tzvetan    | Zielinski |
-- | Saniya     | Kalloufi  |
-- | Sumant     | Peac      |
-- | Duangkaew  | Piveteau  |
-- +------------+-----------+
-- 10 rows in set (0.0034 sec)


SELECT * 
FROM employees
LIMIT 10
;
-- +--------+------------+------------+-----------+--------+------------+
-- | emp_no | birth_date | first_name | last_name | gender | hire_date  |
-- +--------+------------+------------+-----------+--------+------------+
-- |  10001 | 1953-09-02 | Georgi     | Facello   | M      | 1986-06-26 |
-- |  10002 | 1964-06-02 | Bezalel    | Simmel    | F      | 1985-11-21 |
-- |  10003 | 1959-12-03 | Parto      | Bamford   | M      | 1986-08-28 |
-- |  10004 | 1954-05-01 | Chirstian  | Koblick   | M      | 1986-12-01 |
-- |  10005 | 1955-01-21 | Kyoichi    | Maliniak  | M      | 1989-09-12 |
-- |  10006 | 1953-04-20 | Anneke     | Preusig   | F      | 1989-06-02 |
-- |  10007 | 1957-05-23 | Tzvetan    | Zielinski | F      | 1989-02-10 |
-- |  10008 | 1958-02-19 | Saniya     | Kalloufi  | M      | 1994-09-15 |
-- |  10009 | 1952-04-19 | Sumant     | Peac      | F      | 1985-02-18 |
-- |  10010 | 1963-06-01 | Duangkaew  | Piveteau  | F      | 1989-08-24 |
-- +--------+------------+------------+-----------+--------+------------+
-- 10 rows in set (0.0008 sec)


-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8340502#overview
DESCRIBE departments;
-- +-----------+-------------+------+-----+---------+-------+
-- | Field     | Type        | Null | Key | Default | Extra |
-- +-----------+-------------+------+-----+---------+-------+
-- | dept_no   | char(4)     | NO   | PRI | NULL    |       |
-- | dept_name | varchar(40) | NO   | UNI | NULL    |       |
-- +-----------+-------------+------+-----+---------+-------+
-- 2 rows in set (0.0140 sec)

SELECT dept_name FROM departments;
-- +--------------------+
-- | dept_name          |
-- +--------------------+
-- | Customer Service   |
-- | Development        |
-- | Finance            |
-- | Human Resources    |
-- | Marketing          |
-- | Production         |
-- | Quality Management |
-- | Research           |
-- | Sales              |
-- +--------------------+
-- 9 rows in set (0.0033 sec)






























