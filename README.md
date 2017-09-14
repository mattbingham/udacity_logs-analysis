# Logs Analysis Project
This project is part of the Udacity Full Stack Developer Nanodegree.
The goal is to create code capable of displaying the goals listed below, whilst
adhering to SQL and Python (PEP-8) best practices.

## Goals

1. Display the most popular three articles of all time, sorted by most popular first
2. Display the most popular authors of all time, sorted by the most popular first
3. Display which days requests which lead to errors is more than 1%

## Instructions
In order to test this y

## Database information

- The database name is `news`

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

### Goals passing

1.
2.
3.


#### Additional functionality

Views
User input
