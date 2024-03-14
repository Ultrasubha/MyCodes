# IPL data set analytics (using PostgreSQL)
### **Description**
---
>I have used IPL(2008-2017) Dataset 
>* **Objectives**\
	1. Total runs scored by team\
	2. Top batsman for Royal Challengers Bangalore\
	3. Foreign umpire analysis\
	4. Matches played by team by season\
	5. Number of matches played per year for all the years in IPL\
	6. Number of matches won per team per year in IPL\
	7. Extra runs conceded per team in the year 2016\
	8. Top 10 economical bowlers in the year 2015\

### **Setup PostgreSQL**
---
*  To install PostgreSQL:
	```bash
		sudo apt install postgresql postgresql-contrib
		sudo systemctl start postgresql.service
	```

*  To get started with postgres:
	
	```bash
		sudo -i -u postgres psql
	```

*  To create role:
	
	```bash
		create role <username> login
	```
*  To login with new user:
	
	```bash
		psql -u <username> postgres
	```
*  To create a database:
	
	```bash
		CREATE DATABASE <database-name>	
	```
*  To connect with database:
	
	```bash
		\c <database-name>
	```
		
>now your database is created, so you can perform all sql queries on it.
		
		
### **How to run <filename>.sql file**	
---	
* Open a terminal inside the project folder
* Login with the username in postgres and connect with database
* Run the .sql file in postgres promt with this command
		
	```bash
		\i <filename>.sql
	```


### **How to run the project**
* Load the csv and create the tables into the database run:

	```bash
		\i loadcsv.sql
	```
* Run the each solution file :

	```bash
		\i <solution_filename>.sql
	```	
		
>there are 8 solution file please run them one by one in sequence.