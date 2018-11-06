# Logs Analysis Project
Logs Analysis is a project for udacity Full stack Nanodegree course  
It is about building a report tool from a large database by summarizing the data
The database is a PostgreSQL database for a fictional news website.

## Technologies used
* Python
* PostgerSql
* Linux virtual machine

## System Setup Required
* Download and install [vagrant](https://www.vagrantup.com/)
* Download and install [virtualBox](https://www.virtualbox.org/)

## Virtual Machine Setup
* Clone [FSND VM](https://github.com/udacity/fullstack-nanodegree-vm) it contain the vagrant setup
* Open terminal and enter to the vagrant folder that you just clone it then run these command
 * vagrant up
 * vagrant ssh
 * cd /vagrant

## Run The Project
* Clone or download this project
* Add this project inside vagrant folder
* Open Virtual Machine
* To create the database download and unzip newsdata.zip then run  psql -d news -f in the terminal
* create the view listed below
* To run the python file python logs.analysis.py

## App's functionality
Make a report using database to answer three Question  
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Created Views
##### allRequest
```SQL
CREATE VIEW allRequest AS
SELECT time ::date AS day, count(*) AS request
FROM log
GROUP BY day
ORDER BY day;
```
##### allFailuerRequest  
```SQL
CREATE VIEW allFailuerRequest AS
SELECT time ::date AS day, count(*) AS error
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY day
ORDER BY day;

```
