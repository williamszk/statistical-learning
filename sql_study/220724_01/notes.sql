
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

-- ==================================================

mysqlsh -u william
\sql

SHOW DATABASES;
USE sales;

-- An alternative way to specify the primary key
CREATE TABLE sales (
    purchase_number INT NOT NULL AUTO_INCREMENT
    , date_of_purchase DATE NOT NULL 
    , customer_id INT
    , item_code VARCHAR(10)  NOT NULL
    , PRIMARY KEY (purchase_number)
);

DROP TABLE sales;

SHOW TABLES;

DESCRIBE sales;
-- +------------------+-------------+------+-----+---------+----------------+
-- | Field            | Type        | Null | Key | Default | Extra          |
-- +------------------+-------------+------+-----+---------+----------------+
-- | purchase_number  | int         | NO   | PRI | NULL    | auto_increment |
-- | date_of_purchase | date        | NO   |     | NULL    |                |
-- | customer_id      | int         | YES  |     | NULL    |                |
-- | item_code        | varchar(10) | NO   |     | NULL    |                |
-- +------------------+-------------+------+-----+---------+----------------+

-- DDL statemtnt
-- Data Definition Language 
SHOW CREATE TABLE sales;
-- +-------+----------------------------------------------------------------------
-- | Table | Create Table
--                           |
-- +-------+----------------------------------------------------------------------
-- | sales | CREATE TABLE `sales` (
--   `purchase_number` int NOT NULL AUTO_INCREMENT,
--   `date_of_purchase` date NOT NULL,
--   `customer_id` int DEFAULT NULL,
--   `item_code` varchar(10) NOT NULL,
--   PRIMARY KEY (`purchase_number`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
-- +-------+----------------------------------------------------------------------

-- Then, create the “items” table  
-- (columns - data types:  
-- item_code – VARCHAR of 255,  
-- item – VARCHAR of 255,  
-- unit_price – NUMERIC of 10 and 2,  
-- company­_id – VARCHAR of 255),  
-- and the “companies” table  
-- (company_id – VARCHAR of 255,  
-- company_name – VARCHAR of 255,  
-- headquarters_phone_number – integer of 12). 


CREATE TABLE items (
    item_code VARCHAR(255)
    , item VARCHAR(255)
    , unit_price NUMERIC(10,2)
    , company_id VARCHAR(255)
    , PRIMARY KEY (item_code)
);

CREATE TABLE companies (
    company_id VARCHAR(255)
    , company_name VARCHAR(255) 
    , headquarters_phone_number INTEGER(12) 
    , PRIMARY KEY (company_id)
);

SHOW TABLES;
-- +-----------------+
-- | Tables_in_sales |
-- +-----------------+
-- | companies       |
-- | items           |
-- | sales           |
-- +-----------------+

DROP TABLE items;
DROP TABLE companies;

-- FOREIGN KEY Constraint ----------------------------------------------
-- parent table = referenced table
-- child table = referencing table

CREATE TABLE sales (
    purchase_number INT NOT NULL AUTO_INCREMENT
    , date_of_purchase DATE NOT NULL 
    , customer_id INT
    , item_code VARCHAR(10)  NOT NULL
    , PRIMARY KEY (purchase_number)
    , FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE
);

DROP TABLE sales;

-- We need to create the customers table first
-- Or we can add the foreign key later, by altering the existing table

CREATE TABLE sales (
    purchase_number INT NOT NULL AUTO_INCREMENT
    , date_of_purchase DATE NOT NULL 
    , customer_id INT
    , item_code VARCHAR(10)  NOT NULL
    , PRIMARY KEY (purchase_number)
);

ALTER TABLE sales
ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE;

-- we can also drop the foreign key
ALTER TABLE sales
DROP FOREIGN KEY 
-- not finished we need to take a look more on how to do this

-- an exercise to create and remove all tables in the sales database

CREATE TABLE sales (
    purchase_number INT NOT NULL AUTO_INCREMENT
    , date_of_purchase DATE NOT NULL 
    , customer_id INT
    , item_code INT NOT NULL
    , PRIMARY KEY (purchase_number)
);

CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT  
    , first_name VARCHAR(255)
    , last_name VARCHAR(255)
    , email_address VARCHAR(255)
    , number_of_complaints INT
    , PRIMARY KEY (customer_id)
);

CREATE TABLE items (
    item_code INT NOT NULL AUTO_INCREMENT  
    , item VARCHAR(255)
    , unit_price NUMERIC(10,2)
    , company_id INT
    , PRIMARY KEY (item_code)
);

CREATE TABLE companies (
    company_id INT NOT NULL AUTO_INCREMENT  
    , company_name VARCHAR(255) 
    , headquarters_phone_number INTEGER(12) 
    , PRIMARY KEY (company_id)
);

ALTER TABLE sales
ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE;

ALTER TABLE sales
ADD FOREIGN KEY (item_code) REFERENCES items(item_code) ON DELETE CASCADE;

ALTER TABLE items 
ADD FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE;

SHOW TABLES;

SHOW CREATE TABLE sales;
DESCRIBE sales;
DESCRIBE customers;
DESCRIBE items;

DROP TABLE sales;
DROP TABLE customers;
DROP TABLE items;
DROP TABLE companies;

-- about UNIQUE constraint -----------------------------------


CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT  
    , first_name VARCHAR(255)
    , last_name VARCHAR(255)
    , email_address VARCHAR(255)
    , number_of_complaints INT
    , PRIMARY KEY (customer_id)
    , UNIQUE KEY (email_address) -- we add a new constraint
);

-- we can use the ALTER ATBLE command to add the UNIQUE KEY
ALTER TABLE customers
ADD UNIQUE KEY (email_address);

-- Indexes
-- we can add indexes in the table to retrieve the data more easily
-- it is more time consuming to update a table with indexes
-- by default the UNIQUE KEY will an index to a column
-- so it is faster for mysql to retrieve data

-- We can remove the UNIQUE KEY from a table
ALTER TABLE customers
DROP INDEX email_address;

-- exercise

DROP TABLE customers;

CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT  
    , first_name VARCHAR(255)
    , last_name VARCHAR(255)
    , email_address VARCHAR(255)
    , number_of_complaints INT
    , PRIMARY KEY (customer_id)
);

ALTER TABLE customers
ADD COLUMN gender ENUM('M','F') AFTER last_name;

DESCRIBE customers;

INSERT INTO customers (first_name, last_name, gender, email_address, number_of_complaints)
VALUES ('John', 'MacIntosh', 'F', 'john@mac.com', 10);

SELECT * FROM customers;

ALTER TABLE customers
ADD UNIQUE KEY (email_address);

DESCRIBE customers;
-- +----------------------+---------------+------+-----+---------+----------------+
-- | Field                | Type          | Null | Key | Default | Extra          |
-- +----------------------+---------------+------+-----+---------+----------------+
-- | customer_id          | int           | NO   | PRI | NULL    | auto_increment |
-- | first_name           | varchar(255)  | YES  |     | NULL    |                |
-- | last_name            | varchar(255)  | YES  |     | NULL    |                |
-- | gender               | enum('M','F') | YES  |     | NULL    |                |
-- | email_address        | varchar(255)  | YES  | UNI | NULL    |                |
-- | number_of_complaints | int           | YES  |     | NULL    |                |
-- +----------------------+---------------+------+-----+---------+----------------+

-- Next:
-- https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/learn/lecture/8400658#overview

mysqlsh -u william
\sql

USE sales;
SHOW TABLES;

CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT  
    , first_name VARCHAR(255)
    , last_name VARCHAR(255)
    , email_address VARCHAR(255)
    , number_of_complaints INT DEFAULT 0 -- <== here we included the DEFAULT value of 0
    , PRIMARY KEY (customer_id)
);

DESCRIBE customers;
-- +----------------------+--------------+------+-----+---------+----------------+
-- | Field                | Type         | Null | Key | Default | Extra          |
-- +----------------------+--------------+------+-----+---------+----------------+
-- | customer_id          | int          | NO   | PRI | NULL    | auto_increment |
-- | first_name           | varchar(255) | YES  |     | NULL    |                |
-- | last_name            | varchar(255) | YES  |     | NULL    |                |
-- | email_address        | varchar(255) | YES  |     | NULL    |                |
-- | number_of_complaints | int          | YES  |     | 0       |                |
-- +----------------------+--------------+------+-----+---------+----------------+

DROP TABLE customers;

-- We can also include the DEFAULT constraint using the 
-- ALTER statement

CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT  
    , first_name VARCHAR(255)
    , last_name VARCHAR(255)
    , email_address VARCHAR(255)
    , number_of_complaints INT 
    , PRIMARY KEY (customer_id)
);

ALTER TABLE customers
CHANGE COLUMN number_of_complaints number_of_complaints INT DEFAULT 0;

-- DDL statemtnt
-- Data Definition Language 
SHOW CREATE TABLE customers;
-- +-----------+-------------------------------------------------------------
-- | Table     | Create Table
-- +-----------+-------------------------------------------------------------
-- | customers | CREATE TABLE `customers` (
--   `customer_id` int NOT NULL AUTO_INCREMENT,
--   `first_name` varchar(255) DEFAULT NULL,
--   `last_name` varchar(255) DEFAULT NULL,
--   `email_address` varchar(255) DEFAULT NULL,
--   `number_of_complaints` int DEFAULT '0',
--   PRIMARY KEY (`customer_id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
-- +-----------+-------------------------------------------------------------

ALTER TABLE customers
ALTER COLUMN number_of_complaints DROP DEFAULT;





