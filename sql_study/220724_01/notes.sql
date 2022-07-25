
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









