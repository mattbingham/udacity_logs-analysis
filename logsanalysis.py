#!/usr/bin/env python
"""Udacity Logs Analysis project - database connections and queries"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

import psycopg2


DBNAME = "news"


# Return which days had more than 1% request errors
def request_errors():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
  SELECT count(status), count(time) as percentage
  FROM log
  WHERE (log.status LIKE '%404%'
  )
  GROUP BY log.status;
  """)
  print("\nError logs:\n")
  print(c.fetchall())
  # Split code and number
  #print("{} -  total").format(log)

  db.close()

# Return 3 articles sorted by most popular
def popular_articles():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
  SELECT title, count(path) AS num
  FROM articles, log
  WHERE log.path LIKE '/%' || articles.slug
  GROUP BY articles.title
  ORDER BY num DESC
  LIMIT 3;
  """)
  print("\nArticles by Hits:\n")
  articles = (c.fetchall())
  i = 1
  for article in articles:
      print("{}. {} - {} hits total").format(i, article[0], article[1])
      i+=1

  db.close()

# Return all authors, sorted by most popular
def popular_authors():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
  SELECT name, count(path) AS num
  FROM authors, log, articles
  WHERE log.path LIKE '/%' || articles.slug
  AND articles.author = authors.id
  GROUP BY authors.name
  ORDER BY num DESC;
  """)
  print("\nAuthor Leaderboard:\n")
  authors = c.fetchall()

  # Split code and number
  i = 1
  for author in authors:
      print("{}. {} - {} hits total").format(i, author[0], author[1])
      i+=1

  db.close()


if __name__ == "__main__":
  request_errors()
  popular_authors()
  popular_articles()
