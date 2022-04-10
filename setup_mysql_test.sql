-- prepares a MySQL test server for the project
-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- user privileges on hbnb_test_db
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- user privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
