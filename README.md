# Logs Analysis Project
This project is part of the Udacity Full Stack Developer Nanodegree.
The goal is to create a python file that fetches a defined set of results (goals) when executed.

## Goals

1. Display the most popular three articles of all time, sorted by most popular first
2. Display the most popular authors of all time, sorted by the most popular first
3. Display which days requests which lead to errors is more than 1%


## Database information

- The database name is named `news`

### Tables / Columns of news database

| articles |              |
|----------|--------------|
| author   | int          | *References authors(id)*
| title    | text         |
| slug     | text         |
| lead     | text         |
| body     | text         |
| time     | timestamp tz |
| id       | int          |

| authors  |              |
|----------|--------------|
| name     | text         |
| bio      | text         |
| id       | int          |

| log      |              |
|----------|--------------|
| path     | text         |
| ip       | inet         |
| method   | text         |
| status   | text         |
| time     | timestamp tz |
| id       | int          |

## Instructions

This project requires a database and vagrant box supplied by Udacity when participating in this project.

### Required files

1. The vagrant box template is available [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).
2. The newsdata.zip file is available [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
3. You'll also need to install the [psycopg2](http://initd.org/psycopg/docs/) module.

#### Set-up

1. Extract the vagrant box folder
2. Extract newsdata.sql inside the vagrant folder
3. cd into the vagrant folder
4. Start the Vagrant box: Run `vagrant up` (this will begin the box download, which may take a while depending on the speed of your internet connection)
5. Install psycopg2 for Python3
6. Install the database: (Still inside the vagrant folder) run `psql -d news -f newsdata.sql` 

### Run the program

- Run `python logsanalysis.py` in bash (or `python3 logsanalysis.py` if you have both Python2 and 3 installed).

### Goals passing (output)

0. Python file is PEP-8 checked

1. The most popular 3 articles of all time are:
```
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views
```

2. The most popular authors of all time are:
```
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
```

3. Days on which more than 1% of the requests lead to errors:
```
2016-07-17 - 2.3% errors
```