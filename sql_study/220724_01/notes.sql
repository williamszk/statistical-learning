
--  https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8338340#overview

-- $ mysqlsh -u william --py
-- --py starts scripting capabilities to run python

-- https://dev.mysql.com/doc/mysql-shell/8.0/en/mysqlsh.html

-- we need to run this to make mysqlsh run in sql mode
\sql

SHOW DATABASES;
--  MySQL  localhost:33060+ ssl  SQL > SHOW DATABASES;
-- +--------------------+
-- | Database           |
-- +--------------------+
-- | information_schema |
-- | mysql              |
-- | performance_schema |
-- | sys                |
-- +--------------------+
-- 4 rows in set (0.0017 sec)

CREATE DATABASE IF NOT EXISTS sales;
-- we could have used:
-- CREATE SCHEMA IF NOT EXISTS sales;

SHOW DATABASES;
-- +--------------------+
-- | Database           |
-- +--------------------+
-- | information_schema |
-- | mysql              |
-- | performance_schema |
-- | sales              |
-- | sys                |
-- +--------------------+
-- 5 rows in set (0.0015 sec)

-- how to enter into a database?
USE sales;
-- Default schema set to `sales`.
-- Fetching table and column names from `sales` for auto-completion... Press ^C to stop.

-- ===============================================================================
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8339026#overview
-- Data Types
-- STRING
-- alphanumeric datatypes
-- string types: 
--      characters CHAR
--          CHAR(5)    use storage of 5 bytes
--          VARCHAR(5) variable use of characters
--           
-- ENUM
--  ENUM('M','F')
--  limit the options that we can insert

-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8339032#overview 
-- Integers
-- INTEGER, INT, 
-- TINYINT 1 byte
-- SMALLINT 2 bytes
-- MEDIUMINT 3 bytes
-- INT 4 bytes
-- BIGINT 8 bytes
-- all of them can be signed or unsigned, by default MySQL 

-- Precision and Scale:
-- 10.523 -> precision=5
-- 10.523 -> scale=3
-- DECIMAL(5, 3)
--
-- NUMERIC, DECIMAL, both are fixed-point
-- Money should be treated as DECIMAL 
-- DECIMAL(7, 2)
-- 
-- Floating-point numbers
-- This is not precise
-- FLOAT(5,3) 4 bytes, single precision
-- DOUBLE() 8 bytes, double precision

-- DATE     YYYY-MM-DD
-- there is no time in DATE

-- DATETIME YYYY-MM-DD HH:MM:SS[.fraction]

-- TIMESTAMP, number of seconds after 1st January 1970
-- timestamp is better for time zones
-- DATE, DATETIME, TIMESTAMP must be written with quotes


-- BLOB needs to be written in quotes
-- Binary Large Object
CREATE TABLE table_name (
    column_1 data_type constraints
    , column_2 data_type constraints
    , column_3 data_type constraints
);

mysqlsh -u william
\sql

SHOW DATABASES;
USE sales;

CREATE TABLE sales (
    purchase_number INT NOT NULL PRIMARY KEY AUTO_INCREMENT
    , date_of_purchase DATE NOT NULL 
    , customer_id INT
    , item_code VARCHAR(10)  NOT NULL
);

SHOW TABLES;

SELECT * FROM sales.sales;

SELECT * FROM sales;

DROP TABLE sales;

SHOW TABLES;










