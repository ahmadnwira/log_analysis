# FSND-log_analyzer project

## project overview

small log analyzer uses SQL and python to answer some question about popularity and error_rate

## To run the script

`prerequests`

* [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Install Vagrant](https://www.vagrantup.com/intro/getting-started/)
* Download  vagrant image from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

then inside */vagrant* directory unzip the project file
to load the database

* use psql — the PostgreSQL command line program

* -d news — connect to the database named news which has been set up for you
* -f newsdata.sql — run the SQL statements in the file newsdata.sql

> psql -d news -f newsdata.sql

the to run python.

> $ python log.py

**remember to create the views before running the script**

## views

CREATE VIEW day_errors AS
SELECT to_char(time, 'YYYY-MM-DD') as day, count(status) as error FROM log WHERE status LIKE '4%'  group by day;

*day_errors view description*

| day           | error
| ------------- |:----------------:
| yyyy-mm-dd    | number of erros |
| 2016-07-29      | 382           |

CREATE VIEW day_requests AS
SELECT to_char(time, 'YYYY-MM-DD') as day, count(status) as requests from log  group by day ;

*day_errors view description*

| day           | requests
| --------------- |:-------------------:
| yyyy-mm-dd      | number of requests |
| 2016-07-01      | 38705              |