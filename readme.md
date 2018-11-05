# Logs Analysis Project
Logs Analysis is a project for udacity Full stack Nanodegree course  
It is about building a report tool from a large database by summarizing the data.

## Technologies used
* Python
* PostgerSql
* Linux virtual machine

## System Setup Required
* Dawnload and install [vagrant](https://www.vagrantup.com/)
* Dawnload and install [virtualBox](https://www.virtualbox.org/)

## Virtual Machine Setup
* Clone [FSND VM](https://github.com/udacity/fullstack-nanodegree-vm) it contain the vagrant setup
* Open terminal and enter to the vagrant folder that you just clone it then run these command
 * vagrant up
 * vagrent ssh
 * cd /vagrant

## Run The Project
* Clone or download this project
* Add this project inside vagrant folder
* Open Virtual Machine
* To create the database download and unzip newsdata.zip then run  psql -d news -f in the terminal
* To run the python file python logs.analysis.py

## App's functionality
Make a report using database to answer three Question  
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Created Views
##### allRequest
```SQL
create view allRequest as
select time ::date as day, count(*) as request
from log
group by day
order by day;
```
##### allFailuerRequest  
```SQL
create view allFailuerRequest as
select time ::date as day, count(*) as error
from log
where status = '404 NOT FOUND'
group by day
order by day;

```
