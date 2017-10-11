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

This project requires a database and vagrant box supplied by Udacity when participating in this project, so I'm going to go ahead and assume you have this set-up, along with dependenices such as the psycopg2 module.

- Run `python logsanalysis.py` in bash (or `python3 logsanalysis.py` if you have both Python2 and 3 installed).

### Goals passing (output)

0. Python file is PEP-8 checked

1. The most popular 3 articles of all time are:
```
candidate is jerk - 338647
bears love berries - 253801
bad things gone - 170098
```

2. The most popular authors of all time are:
```
Ursula La Multa - 507594
Rudolf von Treppenwitz - 423457
Anonymous Contributor - 170098
Markoff Chaney - 84557
```

3. Days on which more than 1% of the requests lead to errors:
```
2016-07-17 - 2.3% errors
```