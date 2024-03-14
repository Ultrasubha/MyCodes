-- Use master database to drop the database
USE master;

-- Drop the database
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'urahara')
BEGIN
    ALTER DATABASE urahara SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE urahara;
END

-- Drop the user
IF EXISTS (SELECT name FROM sys.server_principals WHERE name = 'urahara')
BEGIN
    DROP LOGIN urahara;
END
