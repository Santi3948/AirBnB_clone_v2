-- prepares a MySQL server for the project
-- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- user privileges on hbnb_dev_db
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- user privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
