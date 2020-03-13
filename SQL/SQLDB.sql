-- Create DB
CREATE DATABASE databasename;

-- Drop DB
DROP DATABASE databasename;

-- Backup DB
BACKUP DATABASE databasename
TO DISK = 'filepath';

-- Create Table
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

-- Drop Table
DROP TABLE Shippers;

--         Alter Table
-- Add column
ALTER TABLE Customers
ADD Email varchar(255);
-- Drop column
ALTER TABLE Customers
DROP COLUMN Email;

ALTER TABLE table_name
ALTER COLUMN column_name datatype;









