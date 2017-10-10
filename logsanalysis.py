#!/usr/bin/env python
"""Udacity Logs Analysis project - database connections and queries"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

import psycopg2

# Script is used to query and return from the "news" database.
# The following answers are required:
# q1. What are the most popular 3 articles of all time?
# q2. Who are the most popular article authors of all time?
# q3. On which days did more than 1% of the requests lead to errors?

# Runs on python3 (I'm using 3.5.2)

import psycopg2
DBNAME = "news"


db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# q1 - Find top 3 articles

c.execute(
    "SELECT path, count(path) \
    FROM log \
    GROUP BY path \
    HAVING path like '/article%' \
    ORDER BY count desc \
    LIMIT 3")

q1 = c.fetchall()

print("\nThe most popular 3 articles of all time are:")
for i in q1:
    article = i[0]
    num = i[1]
    article = article.split("/")[2].split("-")
    articleTitle = " ".join(article)
    print("%s - %s" % (articleTitle, str(num)))

# q2 - Find most popular authors

c.execute(
    "SELECT authors.name, sum(authorcount.count) \
    FROM authors join \
    (SELECT hitcount.count, articles.author \
        FROM \
            (SELECT path, count(path) \
            FROM log \
            GROUP BY path \
            HAVING path like '/article%' \
            ORDER BY count desc limit 8) \
            AS hitcount join articles \
            ON ('/article/' || articles.slug) like hitcount.path) \
    AS authorcount on authorcount.author = authors.id \
    GROUP BY authors.name \
    ORDER BY sum DESC")

q2 = c.fetchall()

print("\nThe most popular authors of all time are:")

for i in q2:
    author = i[0]
    hits = i[1]
    print("%s - %s" % (author, str(hits)))

# q3 - Get dates with errors above 1%

c.execute(
    "SELECT fails.fordate, \
    (cast(fails.failed AS float)/cast(fails.totalhits AS float)*100) AS error \
    FROM (\
        SELECT date(time) AS fordate, count(status) AS totalhits, \
        count(case when status != '200 OK' then 1 else null end) AS failed \
        FROM log GROUP BY fordate ORDER BY fordate) AS fails \
    WHERE cast(fails.failed AS float) / cast(fails.totalhits AS float) > 0.01")

errors = c.fetchall()

print("\nDays on which more than 1% of the requests lead to errors:")
for i in errors:
    date = i[0]
    errors = i[1]
    print("%s - %s%% errors" % (date, str(round(errors, 1))))

db.close()

