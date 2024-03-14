# Company Master - Maharashtra
A data analytics project, where various tasks regarding handling of data and generating insights was performed.
The following tasks were taken care of in the projects.

## Tasks :
### 1. Histogram of Authorized Cap
Plot a histogram on the "Authorized Capital" (column: AUTHORIZED_CAP) with the following intervals

+ <= 1L
+ 1L to 10L
+ 10L to 1Cr
+ 1Cr to 10Cr
+ > 10Cr

Note:
The x-axis labels should be strings listed above, like "<= 1L".
You will have to adjust the intervals if you have an un-balanced plot.

### 2. Bar Plot of company registration by year
From the column, DATE_OF_REGISTRATION parse out the registration year. Using this data, plot a bar plot of the number of company registrations, vs. year.

### 3. Company registration in the year 2015 by the district.
The district can be found by zip code. This resource has that data. Before you start on this problem please make a CSV of zip code vs. district.

In this exercise.
- Only consider registrations for the year 2015.
- Find out the district of registration by the zip code. The zip code can be found at the end of the address column.
- Count the registration by the district.
- Plot a "Bar plot" of "Number of Registration" vs. district.
- If the plot is unbalanced consider plotting only the top districts.

### 4. Grouped Bar Plot
Plot a Grouped Bar Plot by aggregating registration counts over.
- Year of registration
- Principal Business Activity
- Plot only top 5 Prinicipal Business Activity for last 10 years

## Requirements
Technologies like **Python, Matplotlib and Pandas** were used in the project.
Incase you don't have a particular technology installed, you can follow the following commands.

- For Python3 and pip
- - sudo apt update
- - sudo apt install python3
- - sudo apt-get install python3-pip
- - pip install --upgrade pip

You can run the following commands to check if it is installed
- - python3 --version

It is reccommended to check if the path to python is added in the path. This can be done by,
- - echo $PATH
If it doesn't contain the path then perform this command.
- - export PATH=$PATH:/path/to/pip/directory

- For Matplotlib
- - pip install matplotlib

- For Pandas
- - pip install pandas

* You can also download the packages from requirements.txt file. The command for that is - *
- - pip install -r requirements.txt
