#!/usr/bin/env python
import psycopg2

"""Udacity Logs Analysis project - database connections and queries"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

# Script is used to query and return from the "news" database.
# The following answers are required:
# q1. What are the most popular 3 articles of all time?
# q2. Who are the most popular article authors of all time?
# q3. On which days did more than 1% of the requests lead to errors?

# Runs on python3 (I'm using 3.5.2)


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
    article_title = " ".join(article)
    print("%s - %s" % (article_title, str(num)))

# q2 - Find most popular authors

c.execute(
    "SELECT authors.name, sum(author_count.count) \
    FROM authors join \
    (SELECT hit_count.count, articles.author \
        FROM \
            (SELECT path, count(path) \
            FROM log \
            GROUP BY path \
            HAVING path like '/article%' \
            ORDER BY count desc) \
            AS hit_count join articles \
            ON ('/article/' || articles.slug) like hit_count.path) \
    AS author_count on author_count.author = authors.id \
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
    "SELECT fails.for_date, \
    (cast(fails.failed AS float)/cast(fails.all_hits AS float)*100) AS error \
    FROM (\
        SELECT date(time) AS for_date, count(status) AS all_hits, \
        count(case when status != '200 OK' then 1 else null end) AS failed \
        FROM log GROUP BY for_date ORDER BY for_date) AS fails \
    WHERE cast(fails.failed AS float) / cast(fails.all_hits AS float) > 0.01")

errors = c.fetchall()

print("\nDays on which more than 1% of the requests lead to errors:")
for i in errors:
    date = i[0]
    errors = i[1]
    print("%s - %s%% errors" % (date, str(round(errors, 1))))

db.close()
