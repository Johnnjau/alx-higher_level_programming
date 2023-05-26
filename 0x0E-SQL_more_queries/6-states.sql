-- Creates the table 'states' in the 'hbtn_0d_usa' database.
-- The table will have an auto-increment primary key and a name column.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Rest of your SQL statements for creating the 'states' table
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);
