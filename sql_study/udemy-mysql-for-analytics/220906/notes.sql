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


-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8344766?start=0#overview

-- start mysql shell 
mysqlsh -u william
-- the password for the local mysql
mNpL9UwjEPFxTpGjRdnvDbAvrqvVGNxs48LAEWAu
yes
-- change to sql terminal
\sql


-- get all people that are named Denis
SELECT * FROM employees WHERE first_name = 'Denis';
-- +--------+------------+------------+----------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name      | gender | hire_date  |
-- +--------+------------+------------+----------------+--------+------------+
-- |  11688 | 1958-09-04 | Denis      | Coullard       | F      | 1994-10-29 |
-- |  15083 | 1958-11-24 | Denis      | Nicolson       | M      | 1994-03-02 |
-- |  15824 | 1957-07-28 | Denis      | Schwabacher    | F      | 1988-02-14 |
-- ........
-- | 496944 | 1954-09-02 | Denis      | Fortenbacher   | M      | 1986-02-09 |
-- | 497292 | 1964-05-28 | Denis      | Gustavson      | M      | 1990-07-25 |
-- | 498260 | 1959-04-15 | Denis      | Fetvedt        | F      | 1988-05-04 |
-- +--------+------------+------------+----------------+--------+------------+
-- 232 rows in set (0.3929 sec)



SELECT * FROM employees WHERE first_name = 'Elvis';
-- +--------+------------+------------+----------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name      | gender | hire_date  |
-- +--------+------------+------------+----------------+--------+------------+
-- |  10030 | 1958-07-14 | Elvis      | Demeyer        | M      | 1994-02-17 |
-- |  11050 | 1952-09-23 | Elvis      | Katiyar        | M      | 1986-05-06 |
-- |  12870 | 1960-03-24 | Elvis      | Pfau           | F      | 1990-04-09 |
-- |  13620 | 1956-10-31 | Elvis      | Dolinsky       | M      | 1985-06-12 |
-- ...............
-- | 494489 | 1952-06-21 | Elvis      | Kroll          | M      | 1994-11-22 |
-- | 495295 | 1961-10-14 | Elvis      | Lamma          | M      | 1994-02-28 |
-- | 495406 | 1956-05-04 | Elvis      | Gerlach        | M      | 1990-09-17 |
-- | 496503 | 1956-09-01 | Elvis      | Verhoeff       | M      | 1986-10-27 |
-- | 497910 | 1961-05-12 | Elvis      | Cannard        | F      | 1990-09-23 |
-- | 498621 | 1955-09-07 | Elvis      | Zykh           | M      | 1993-08-31 |
-- | 499091 | 1952-09-24 | Elvis      | Kohling        | F      | 1986-02-25 |
-- +--------+------------+------------+----------------+--------+------------+
-- 246 rows in set (0.3526 sec)

-- equal operator
-- examples of operators that we can use inside the WHERE clause
-- AND
-- OR 
-- IN 
-- NOT IN 
-- LIKE 
-- NOT LIKE
-- BETWEEN...  AND...
-- EXISTS
-- NOT EXISTS
-- IS NULL
-- IS NOT NULL
-- comparison operators 

-- get all employees whose firstname is Denis and is male
SELECT * FROM employees WHERE first_name='Denis' AND gender='M';
-- +--------+------------+------------+----------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name      | gender | hire_date  |
-- +--------+------------+------------+----------------+--------+------------+
-- |  15083 | 1958-11-24 | Denis      | Nicolson       | M      | 1994-03-02 |
-- |  17224 | 1955-04-06 | Denis      | Back           | M      | 1985-07-29 |
-- |  18121 | 1953-08-26 | Denis      | Stanfel        | M      | 1990-05-21 |
-- |  18187 | 1965-01-08 | Denis      | Falster        | M      | 1989-10-12 |
-- |  19798 | 1962-12-22 | Denis      | Schmezko       | M      | 1986-10-30 |
-- .....
-- | 489646 | 1954-12-22 | Denis      | Heering        | M      | 1991-03-27 |
-- | 490493 | 1956-07-06 | Denis      | Auyong         | M      | 1989-04-15 |
-- | 490839 | 1958-06-19 | Denis      | Narwekar       | M      | 1987-12-09 |
-- | 491095 | 1962-05-30 | Denis      | Kuszyk         | M      | 1992-12-05 |
-- | 496944 | 1954-09-02 | Denis      | Fortenbacher   | M      | 1986-02-09 |
-- | 497292 | 1964-05-28 | Denis      | Gustavson      | M      | 1990-07-25 |
-- +--------+------------+------------+----------------+--------+------------+
-- 140 rows in set (0.2038 sec)

-- Retrieve a list with all female employees whose first name is Kellie. 

SELECT * FROM employees WHERE first_name='Kellie' AND gender='F';

-- +--------+------------+------------+-----------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name       | gender | hire_date  |
-- +--------+------------+------------+-----------------+--------+------------+
-- |  10225 | 1957-02-13 | Kellie     | Chinen          | F      | 1986-06-19 |
-- |  14918 | 1962-10-16 | Kellie     | Kaiserswerth    | F      | 1986-11-18 |
-- |  22164 | 1957-04-05 | Kellie     | Argence         | F      | 1989-09-09 |
-- ...........
-- | 479492 | 1952-02-03 | Kellie     | Beutelspacher   | F      | 1988-05-18 |
-- | 481078 | 1963-08-18 | Kellie     | Simkin          | F      | 1987-02-02 |
-- | 487020 | 1960-08-12 | Kellie     | Busillo         | F      | 1985-05-09 |
-- | 492681 | 1957-04-06 | Kellie     | Koshino         | F      | 1991-03-28 |
-- | 494867 | 1953-08-24 | Kellie     | Chenney         | F      | 1987-06-28 |
-- +--------+------------+------------+-----------------+--------+------------+
-- 86 rows in set (0.3347 sec)


-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8344962#overview
-- 
SELECT * FROM employees WHERE first_name='Denis' OR first_name='Elvis';
-- +--------+------------+------------+----------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name      | gender | hire_date  |
-- +--------+------------+------------+----------------+--------+------------+
-- |  10030 | 1958-07-14 | Elvis      | Demeyer        | M      | 1994-02-17 |
-- |  11050 | 1952-09-23 | Elvis      | Katiyar        | M      | 1986-05-06 |
-- ....
-- | 497292 | 1964-05-28 | Denis      | Gustavson      | M      | 1990-07-25 |
-- | 497910 | 1961-05-12 | Elvis      | Cannard        | F      | 1990-09-23 |
-- | 498260 | 1959-04-15 | Denis      | Fetvedt        | F      | 1988-05-04 |
-- | 498621 | 1955-09-07 | Elvis      | Zykh           | M      | 1993-08-31 |
-- | 499091 | 1952-09-24 | Elvis      | Kohling        | F      | 1986-02-25 |
-- +--------+------------+------------+----------------+--------+------------+
-- 478 rows in set (0.2760 sec)


-- Retrieve a list with all employees whose first name is either Kellie or Aruna.
SELECT * FROM employees WHERE first_name='Kellie' OR first_name='Aruna';
-- +--------+------------+------------+-----------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name       | gender | hire_date  |
-- +--------+------------+------------+-----------------+--------+------------+
-- |  10225 | 1957-02-13 | Kellie     | Chinen          | F      | 1986-06-19 |
-- |  10789 | 1964-05-19 | Aruna      | Journel         | F      | 1987-02-02 |
-- |  11217 | 1954-07-01 | Kellie     | Mawatari        | M      | 1987-09-22 |
-- ....
-- | 494745 | 1962-09-16 | Aruna      | Massonet        | F      | 1993-09-10 |
-- | 494867 | 1953-08-24 | Kellie     | Chenney         | F      | 1987-06-28 |
-- | 498321 | 1956-11-26 | Aruna      | Kavvadias       | M      | 1987-07-01 |
-- +--------+------------+------------+-----------------+--------+------------+
-- 432 rows in set (0.2253 sec)

-- Operator Precedence
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345096#overview
-- AND has precedence over or
-- we can use parenthesis to change the precedence of execution
-- there are some records that do not have gender
-- get all cases of non-missing gender for people called Denis
-- and compare them with the whole list of people called Denis
-- for people called Denis, how many missing gender are there?

SELECT COUNT(*) FROM employees WHERE first_name='Denis';
-- +----------+
-- | COUNT(*) |
-- +----------+
-- |      232 |
-- +----------+
-- 1 row in set (0.3236 sec)

SELECT COUNT(*) FROM employees WHERE first_name='Denis' AND (gender='F' OR gender='M');
-- +----------+
-- | COUNT(*) |
-- +----------+
-- |      232 |
-- +----------+
-- 1 row in set (0.1637 sec)

-- They are the same number.

-- Are there any cases of missing gender?
DESCRIBE employees;
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
-- 6 rows in set (0.0154 sec)

-- gender is nullable

SELECT COUNT(*) FROM employees;
-- +----------+
-- | COUNT(*) |
-- +----------+
-- |   300024 |
-- +----------+
-- 1 row in set (14.3656 sec)

SELECT COUNT(*) FROM employees WHERE (gender='M' OR gender='F');
-- +----------+
-- | COUNT(*) |
-- +----------+
-- |   300024 |
-- +----------+
-- 1 row in set (0.1752 sec)

-- Interestingly the seconds query was very fast...
-- why is that?

-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8755140#overview
-- Retrieve a list with all female employees whose first name is either Kellie or Aruna

SELECT * FROM employees WHERE (first_name='Kellie' OR first_name='Aruna') AND gender='F';
-- +--------+------------+------------+-----------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name       | gender | hire_date  |
-- +--------+------------+------------+-----------------+--------+------------+
-- |  10225 | 1957-02-13 | Kellie     | Chinen          | F      | 1986-06-19 |
-- |  10789 | 1964-05-19 | Aruna      | Journel         | F      | 1987-02-02 |
-- |  12038 | 1956-04-13 | Aruna      | Businaro        | F      | 1987-01-09 |
-- |  14080 | 1957-02-24 | Aruna      | Motley          | F      | 1987-03-09 |
-- |  14459 | 1964-09-21 | Aruna      | Boreale         | F      | 1986-12-06 |
-- ..........
-- | 488181 | 1960-05-02 | Aruna      | Delgrande       | F      | 1986-12-15 |
-- | 492681 | 1957-04-06 | Kellie     | Koshino         | F      | 1991-03-28 |
-- | 494745 | 1962-09-16 | Aruna      | Massonet        | F      | 1993-09-10 |
-- | 494867 | 1953-08-24 | Kellie     | Chenney         | F      | 1987-06-28 |
-- +--------+------------+------------+-----------------+--------+------------+
-- 167 rows in set (0.3797 sec)

-- Next topic
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345098#overview
-- IN, NOT IN
-- find all employees that have first name as Cathie, Mark and Nathan
SELECT * FROM employees WHERE 
       first_name='Cathe'
    OR first_name='Mark'
    OR first_name='Nathan'
;
-- +--------+------------+------------+------------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name        | gender | hire_date  |
-- +--------+------------+------------+------------------+--------+------------+
-- |  10135 | 1956-12-23 | Nathan     | Monkewich        | M      | 1988-02-19 |
-- |  10415 | 1957-11-12 | Mark       | Coorg            | M      | 1993-10-25 |
-- |  11095 | 1961-12-31 | Nathan     | Flowers          | M      | 1994-05-28 |
-- ...
-- | 497568 | 1958-11-19 | Mark       | Boissier         | M      | 1988-02-07 |
-- | 498201 | 1952-03-22 | Mark       | Schahn           | F      | 1990-12-24 |
-- | 498917 | 1955-12-28 | Nathan     | Papadias         | F      | 1987-01-09 |
-- | 499834 | 1956-04-04 | Nathan     | Chimia           | F      | 1995-05-12 |
-- | 499986 | 1952-07-22 | Nathan     | Ranta            | F      | 1985-08-11 |
-- +--------+------------+------------+------------------+--------+------------+
-- 470 rows in set (0.3393 sec)

-- A more concise way to express the same query
SELECT * FROM employees WHERE 
    first_name IN ('Cathe', 'Mark', 'Nathan');
-- this is faster

-- Select all employees that do not have the following names:
SELECT * FROM employees WHERE 
    first_name NOT IN ('Cathe', 'Mark', 'Nathan');

-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8340510#overview
-- Use the IN operator to select all individuals from the “employees” table, whose first name is either “Denis”, or “Elvis”.
SELECT * FROM employees WHERE first_name IN ('Denis', 'Elvis');

-- Extract all records from the ‘employees’ table, aside from those with employees named John, Mark, or Jacob
SELECT * FROM employees
    WHERE first_name NOT IN (
        'Denis'
        , 'Elvis'
    );

-- LIKE and NOT LIKE
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345106#overview
-- the LIKE operator is used with the WHERE clause
-- it is used to find matches in a pattern

-- find all records where the first name starts with Mar
SELECT * FROM employees
    WHERE first_name LIKE('Mar%');
-- % acts like a wildcard for 0 or more letters tha comes after it
-- we can use _ underscore to match just one character in the pattern matching

-- find all records where the first name starts with "Mar", and 
-- the first name has 4 letters
SELECT * FROM employees
    WHERE first_name LIKE('Mar_');
-- +--------+------------+------------+------------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name        | gender | hire_date  |
-- +--------+------------+------------+------------------+--------+------------+
-- |  10011 | 1953-11-07 | Mary       | Sluis            | F      | 1990-01-22 |
-- |  10196 | 1954-01-27 | Marc       | Hellwagner       | M      | 1994-11-16 |
-- ....
-- | 240298 | 1954-06-27 | Mara       | Munke            | M      | 1991-07-01 |
-- | 240321 | 1955-08-19 | Mary       | Bugaenko         | M      | 1990-01-11 |
-- +--------+------------+------------+------------------+--------+------------+
-- 1630 rows in set (0.2243 sec)


-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8340512#overview
-- Working with the “employees” table, use the LIKE operator to select the data about all individuals, whose first name starts with “Mark”; specify that the name can be succeeded by any sequence of characters.
SELECT * FROM employees WHERE first_name LIKE('Mark%');
-- +--------+------------+------------+------------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name        | gender | hire_date  |
-- +--------+------------+------------+------------------+--------+------------+
-- |  10232 | 1956-03-11 | Marko      | Auria            | F      | 1992-06-04 |
-- |  10415 | 1957-11-12 | Mark       | Coorg            | M      | 1993-10-25 |
-- |  10522 | 1955-07-24 | Marke      | Cesareni         | F      | 1986-12-12 |
-- |  11887 | 1957-05-25 | Marke      | Kragelund        | M      | 1994-10-17 |
-- |  12007 | 1952-06-18 | Marko      | Dehkordi         | M      | 1989-05-17 |
-- .....
-- | 498980 | 1957-05-29 | Marko      | Eppinger         | M      | 1988-07-13 |
-- | 499451 | 1953-04-28 | Marko      | Goldhammer       | M      | 1986-10-19 |
-- | 499620 | 1961-07-30 | Marke      | Ibel             | F      | 1996-01-30 |
-- +--------+------------+------------+------------------+--------+------------+
-- 690 rows in set (0.3888 sec)

-- Retrieve a list with all employees who have been hired in the year 2000.
SELECT * FROM employees WHERE hire_date LIKE('2000%');
-- +--------+------------+-------------+------------+--------+------------+
-- | emp_no | birth_date | first_name  | last_name  | gender | hire_date  |
-- +--------+------------+-------------+------------+--------+------------+
-- |  47291 | 1960-09-09 | Ulf         | Flexer     | M      | 2000-01-12 |
-- |  60134 | 1964-04-21 | Seshu       | Rathonyi   | F      | 2000-01-02 |
-- |  72329 | 1953-02-09 | Randi       | Luit       | F      | 2000-01-02 |
-- | 108201 | 1955-04-14 | Mariangiola | Boreale    | M      | 2000-01-01 |
-- | 205048 | 1960-09-12 | Ennio       | Alblas     | F      | 2000-01-06 |
-- | 222965 | 1959-08-07 | Volkmar     | Perko      | F      | 2000-01-13 |
-- | 226633 | 1958-06-10 | Xuejun      | Benzmuller | F      | 2000-01-04 |
-- | 227544 | 1954-11-17 | Shahab      | Demeyer    | M      | 2000-01-08 |
-- | 422990 | 1953-04-09 | Jaana       | Verspoor   | F      | 2000-01-11 |
-- | 424445 | 1953-04-27 | Jeong       | Boreale    | M      | 2000-01-03 |
-- | 428377 | 1957-05-09 | Yucai       | Gerlach    | M      | 2000-01-23 |
-- | 463807 | 1964-06-12 | Bikash      | Covnot     | M      | 2000-01-28 |
-- | 499553 | 1954-05-06 | Hideyuki    | Delgrande  | F      | 2000-01-22 |
-- +--------+------------+-------------+------------+--------+------------+
-- 13 rows in set (0.3127 sec)


-- Retrieve a list with all employees whose employee number is written with 5 characters, and starts with “1000”. 
SELECT * FROM employees WHERE emp_no LIKE('1000_');
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
-- +--------+------------+------------+-----------+--------+------------+
-- 9 rows in set (0.3175 sec)


-- wildcard characters
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345112#overview

-- Extract all individuals from the ‘employees’ table whose first name contains “Jack”.
-- Once you have done that, extract another list containing the names of employees that do not contain “Jack”.

SELECT first_name FROM employees WHERE first_name LIKE('%jack%');

SELECT first_name FROM employees WHERE first_name NOT LIKE('%jack%');

-- Next:
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345114#overview
-- the operator BETWEEN... END...
-- used with the WHERE clause 

SELECT * FROM employees WHERE hire_date BETWEEN '1990-01-01' AND '2000-01-01';
-- +--------+------------+----------------+------------------+--------+------------+
-- | emp_no | birth_date | first_name     | last_name        | gender | hire_date  |
-- +--------+------------+----------------+------------------+--------+------------+
-- |  10007 | 1958-02-19 | Saniya         | Kalloufi         | M      | 1994-09-15 |
-- |  10010 | 1953-11-07 | Mary           | Sluis            | F      | 1990-01-22 |
-- |  10011 | 1960-10-04 | Patricio       | Bridgland        | M      | 1992-12-18 |
-- |  10015 | 1961-05-02 | Kazuhito       | Cappelletti      | M      | 1995-01-27 |
-- ....
-- |  13335 | 1963-03-11 | Vatsa          | Hofman           | M      | 1991-07-29 |
-- |  13338 | 1962-03-24 | Mart           | Koblitz          | M      | 1990-08-24 |
-- +--------+------------+----------------+------------------+--------+------------+
-- 135214 rows in set (0.0065 sec)

-- we can also use NOT BETWEEN... AND...

DESCRIBE employees;
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
-- 6 rows in set (0.0114 sec)

-- note that hire_date is of "date" type

-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8340844#overview

--  MySQL  localhost:33060+ ssl  employees  SQL > describe salaries
--                                             -> ;   
-- +-----------+------+------+-----+---------+-------+
-- | Field     | Type | Null | Key | Default | Extra |
-- +-----------+------+------+-----+---------+-------+
-- | emp_no    | int  | NO   | PRI | NULL    |       |
-- | salary    | int  | NO   |     | NULL    |       |
-- | from_date | date | NO   | PRI | NULL    |       |
-- | to_date   | date | NO   |     | NULL    |       |
-- +-----------+------+------+-----+---------+-------+
-- 4 rows in set (0.0028 sec)

-- Select all the information from the “salaries” table regarding contracts from 66,000 to 70,000 dollars per year.
SELECT * FROM salaries WHERE salary BETWEEN 66000 AND 70000;
-- +--------+--------+------------+------------+
-- | emp_no | salary | from_date  | to_date    |
-- +--------+--------+------------+------------+
-- |  10001 |  66074 | 1988-06-25 | 1989-06-25 |
-- |  10001 |  66596 | 1989-06-25 | 1990-06-25 |
-- |  10001 |  66961 | 1990-06-25 | 1991-06-25 |
-- |  10002 |  67534 | 1998-08-03 | 1999-08-03 |
-- |  10002 |  69366 | 1999-08-03 | 2000-08-02 |
-- |  10004 |  67096 | 1998-11-28 | 1999-11-28 |
-- ...............
-- |  10431 |  67068 | 1987-10-08 | 1988-10-07 |
-- |  10431 |  68188 | 1988-10-07 | 1989-10-07 |
-- +--------+--------+------------+------------+
-- 74027 rows in set (0.0411 sec)


-- Retrieve a list with all individuals whose employee number is not between ‘10004’ and ‘10012’.
SELECT * FROM employees WHERE emp_no NOT BETWEEN '10004' AND '10012';
-- +--------+------------+----------------+------------------+--------+------------+
-- | emp_no | birth_date | first_name     | last_name        | gender | hire_date  |
-- +--------+------------+----------------+------------------+--------+------------+
-- |  10001 | 1953-09-02 | Georgi         | Facello          | M      | 1986-06-26 |
-- |  10002 | 1964-06-02 | Bezalel        | Simmel           | F      | 1985-11-21 |
-- |  10003 | 1959-12-03 | Parto          | Bamford          | M      | 1986-08-28 |
-- |  10013 | 1963-06-07 | Eberhardt      | Terkki           | M      | 1985-10-20 |
-- |  10014 | 1956-02-12 | Berni          | Genin            | M      | 1987-03-11 |
-- ....
-- |  10816 | 1958-02-24 | Morris         | Caine            | F      | 1989-06-27 |
-- |  10817 | 1958-10-02 | Uri            | Rullman          | F      | 1990-12-26 |
-- +--------+------------+----------------+------------------+--------+------------+
-- 300015 rows in set (0.0107 sec)
-- Result printing interrupted, rows may be missing from the output.


-- Select the names of all departments with numbers between ‘d003’ and ‘d006’.
DESCRIBE departments; 
-- +-----------+-------------+------+-----+---------+-------+
-- | Field     | Type        | Null | Key | Default | Extra |
-- +-----------+-------------+------+-----+---------+-------+
-- | dept_no   | char(4)     | NO   | PRI | NULL    |       |
-- | dept_name | varchar(40) | NO   | UNI | NULL    |       |
-- +-----------+-------------+------+-----+---------+-------+
-- 2 rows in set (0.0054 sec)

SELECT * FROM departments WHERE dept_no BETWEEN 'd003' AND 'd006';
-- +---------+--------------------+
-- | dept_no | dept_name          |
-- +---------+--------------------+
-- | d003    | Human Resources    |
-- | d004    | Production         |
-- | d005    | Development        |
-- | d006    | Quality Management |
-- +---------+--------------------+
-- 4 rows in set (0.0049 sec)

-- Next
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345126#overview


-- start mysql shell 
mysqlsh -u william
-- the password for the local mysql
mNpL9UwjEPFxTpGjRdnvDbAvrqvVGNxs48LAEWAu
yes
-- change to sql terminal
\sql

USE employees;

SELECT * FROM employees WHERE first_name IS NULL;
-- empty set

-- Select the names of all departments whose department number value is not null.
SELECT * FROM departments WHERE dept_no IS NOT NULL;


-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345142#overview
-- for not equal operators we can use <> or !=

-- get all employees that were hired after 2000
SELECT * FROM employees WHERE hire_date > '2000-01-01';
-- +--------+------------+------------+------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name  | gender | hire_date  |
-- +--------+------------+------------+------------+--------+------------+
-- |  47291 | 1960-09-09 | Ulf        | Flexer     | M      | 2000-01-12 |
-- |  60134 | 1964-04-21 | Seshu      | Rathonyi   | F      | 2000-01-02 |
-- |  72329 | 1953-02-09 | Randi      | Luit       | F      | 2000-01-02 |
-- | 205048 | 1960-09-12 | Ennio      | Alblas     | F      | 2000-01-06 |
-- | 222965 | 1959-08-07 | Volkmar    | Perko      | F      | 2000-01-13 |
-- | 226633 | 1958-06-10 | Xuejun     | Benzmuller | F      | 2000-01-04 |
-- | 227544 | 1954-11-17 | Shahab     | Demeyer    | M      | 2000-01-08 |
-- | 422990 | 1953-04-09 | Jaana      | Verspoor   | F      | 2000-01-11 |
-- | 424445 | 1953-04-27 | Jeong      | Boreale    | M      | 2000-01-03 |
-- | 428377 | 1957-05-09 | Yucai      | Gerlach    | M      | 2000-01-23 |
-- | 463807 | 1964-06-12 | Bikash     | Covnot     | M      | 2000-01-28 |
-- | 499553 | 1954-05-06 | Hideyuki   | Delgrande  | F      | 2000-01-22 |
-- +--------+------------+------------+------------+--------+------------+
-- 12 rows in set (0.3200 sec)



SELECT * FROM employees WHERE hire_date < '1985-02-01';
-- +--------+------------+-------------+--------------+--------+------------+
-- | emp_no | birth_date | first_name  | last_name    | gender | hire_date  |
-- +--------+------------+-------------+--------------+--------+------------+
-- | 110022 | 1956-09-12 | Margareta   | Markovitch   | M      | 1985-01-01 |
-- | 110085 | 1959-10-28 | Ebru        | Alpin        | M      | 1985-01-01 |
-- | 110114 | 1957-03-28 | Isamu       | Legleitner   | F      | 1985-01-14 |
-- | 110183 | 1953-06-24 | Shirish     | Ossenbruggen | F      | 1985-01-01 |
-- | 110303 | 1956-06-08 | Krassimir   | Wegerle      | F      | 1985-01-01 |
-- | 110511 | 1957-07-08 | DeForest    | Hagimont     | M      | 1985-01-01 |
-- | 110725 | 1961-03-14 | Peternela   | Onuegbe      | F      | 1985-01-01 |
-- | 111035 | 1962-02-24 | Przemyslawa | Kaelbling    | M      | 1985-01-01 |
-- | 111400 | 1959-11-09 | Arie        | Staelin      | M      | 1985-01-01 |
-- | 111692 | 1954-10-05 | Tonny       | Butterworth  | F      | 1985-01-01 |
-- +--------+------------+-------------+--------------+--------+------------+
-- 10 rows in set (0.3181 sec)


-- Retrieve a list with data about all female employees who were hired in the year 2000 or after.
-- Hint: If you solve the task correctly, SQL should return 7 rows.

SELECT * FROM employees WHERE gender='F' AND hire_date >= '2000-01-01';
-- +--------+------------+------------+------------+--------+------------+
-- | emp_no | birth_date | first_name | last_name  | gender | hire_date  |
-- +--------+------------+------------+------------+--------+------------+
-- |  60134 | 1964-04-21 | Seshu      | Rathonyi   | F      | 2000-01-02 |
-- |  72329 | 1953-02-09 | Randi      | Luit       | F      | 2000-01-02 |
-- | 205048 | 1960-09-12 | Ennio      | Alblas     | F      | 2000-01-06 |
-- | 222965 | 1959-08-07 | Volkmar    | Perko      | F      | 2000-01-13 |
-- | 226633 | 1958-06-10 | Xuejun     | Benzmuller | F      | 2000-01-04 |
-- | 422990 | 1953-04-09 | Jaana      | Verspoor   | F      | 2000-01-11 |
-- | 499553 | 1954-05-06 | Hideyuki   | Delgrande  | F      | 2000-01-22 |
-- +--------+------------+------------+------------+--------+------------+
-- 7 rows in set (0.2035 sec)


-- Extract a list with all employees’ salaries higher than $150,000 per annum.
SELECT * FROM salaries WHERE salary > 150000;
-- +--------+--------+------------+------------+
-- | emp_no | salary | from_date  | to_date    |
-- +--------+--------+------------+------------+
-- |  43624 | 151115 | 1998-03-23 | 1999-03-23 |
-- |  43624 | 153166 | 1999-03-23 | 2000-03-22 |
-- |  43624 | 153458 | 2000-03-22 | 2001-03-22 |
-- |  43624 | 157821 | 2001-03-22 | 2002-03-22 |
-- |  43624 | 158220 | 2002-03-22 | 9999-01-01 |
-- |  46439 | 150345 | 2002-05-15 | 9999-01-01 |
-- |  47978 | 151929 | 2001-07-14 | 2002-07-14 |
-- |  47978 | 155709 | 2002-07-14 | 9999-01-01 |
-- |  66793 | 150052 | 2002-06-16 | 9999-01-01 |
-- |  80823 | 151768 | 2001-02-22 | 2002-02-22 |
-- |  80823 | 154459 | 2002-02-22 | 9999-01-01 |
-- | 109334 | 151484 | 1998-02-12 | 1999-02-12 |
-- | 109334 | 154885 | 1999-02-12 | 2000-02-12 |
-- | 109334 | 155377 | 2000-02-12 | 2001-02-11 |
-- | 109334 | 154888 | 2001-02-11 | 2002-02-11 |
-- | 109334 | 155190 | 2002-02-11 | 9999-01-01 |
-- +--------+--------+------------+------------+
-- 16 rows in set (0.4967 sec)


-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345160#overview
-- SELECT DISTINCT
SELECT DISTINCT gender FROM employees;
-- +--------+
-- | gender |
-- +--------+
-- | M      |
-- | F      |
-- +--------+
-- 2 rows in set (0.2078 sec)

-- Obtain a list with all different “hire dates” from the “employees” table.
-- Expand this list and click on “Limit to 1000 rows”. This way you will set the limit of output rows displayed back to the default of 1000.
-- In the next lecture, we will show you how to manipulate the limit rows count. 

SELECT DISTINCT hire_date FROM employees;
-- +------------+
-- | hire_date  |
-- +------------+
-- | 1986-06-26 |
-- | 1985-11-21 |
-- | 1986-08-28 |
-- ....
-- | 1999-12-12 |
-- | 1999-07-08 |
-- | 1999-09-15 |
-- | 1999-11-26 |
-- | 2000-01-22 |
-- +------------+
-- 5434 rows in set (0.4003 sec)

-- Aggregate Function
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345176#overview
-- COUNT(), count of non-null values in a field
-- SUM()
-- MIN()
-- MAX()
-- AVG()

-- How to count including the null values?
-- We can count the index, which is not nullable

-- how many employees are registered in the database?
SELECT COUNT(emp_no) FROM employees;
-- +---------------+
-- | COUNT(emp_no) |
-- +---------------+
-- |        300024 |
-- +---------------+
-- 1 row in set (14.3672 sec)

-- how many distinct first names do we have in the database?
SELECT COUNT(DISTINCT first_name) FROM employees;
-- +----------------------------+
-- | COUNT(DISTINCT first_name) |
-- +----------------------------+
-- |                       1275 |
-- +----------------------------+
-- 1 row in set (0.2981 sec)


-- How many annual contracts with a value higher than or equal to $100,000 have been registered in the salaries table?
SELECT COUNT(emp_no) FROM salaries WHERE salary >= 100000;
-- +---------------+
-- | COUNT(emp_no) |
-- +---------------+
-- |         32207 |
-- +---------------+
-- 1 row in set (0.3401 sec)



-- How many managers do we have in the “employees” database? Use the star symbol (*) in your code to solve this exercise.
SELECT COUNT(*) FROM dept_manager;
-- +----------+
-- | COUNT(*) |
-- +----------+
-- |       24 |
-- +----------+
-- 1 row in set (0.0143 sec)


-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345178#overview
-- get the employees table and show in descending order on the first_name
SELECT * FROM employees ORDER BY first_name DESC;
-- ascending is the default. we could use ASC to make it explicit.

-- we can sort by two or more fields
SELECT * FROM employees ORDER BY first_name, last_name DESC;

-- Select all data from the “employees” table, ordering it by “hire date” in descending order.
SELECT * FROM employees ORDER BY hire_date DESC;

-- GROUP BY
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8345180#overview
















