-- Create a new login/user
CREATE LOGIN urahara 
WITH PASSWORD = 'urahara';

-- Create a new database
CREATE DATABASE urahara;

-- Use the newly created database
USE urahara;

-- Create a user in the database mapped to the login
CREATE USER urahara FOR LOGIN urahara;

-- Assign the user as the owner of the database
ALTER AUTHORIZATION ON DATABASE::YourDatabase TO YourUsername;

\conninfo