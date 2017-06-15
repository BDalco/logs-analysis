#!/usr/bin/env python3

import psycopg2
from datetime import date


def connect():
    """ Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


def executeQuery(query):
    """ Execute query to get the answers """
    db, cursor = connect()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def topArticles():
    """ What are the most popular three articles of all time? """
    query = """
            SELECT articles.title, count(*) AS views
            FROM articles, log
            WHERE log.path = CONCAT('/article/', articles.slug)
            AND status = '200 OK'
            GROUP BY articles.title ORDER BY views DESC LIMIT 3
            """
    topThreeArticles = executeQuery(query)
    print('What are the most popular three articles of all time?')
    for i in topThreeArticles:
        print('"' + i[0] + '" - ' + str(i[1]) + ' views')


def topAuthors():
    """ Who are the most popular article authors of all time? """
    query = """
            SELECT authors.name, count(*) AS views
            FROM articles, authors, log
            WHERE authors.id = articles.author
            AND log.path = CONCAT('/article/', articles.slug)
            AND status = '200 OK'
            GROUP BY authors.name ORDER BY views DESC
            """
    topArticleAuthors = executeQuery(query)
    print('Who are the most popular article authors of all time?')
    for i in topArticleAuthors:
        print(i[0] + ' - ' + str(i[1]) + ' views')


def errorDays():
    """ On which days did more than 1% of requests lead to errors? """
    query = """
            SELECT date, ROUND((errorLog * 1.0/allLog)*100, 2) AS percentage
            FROM (SELECT date(time),
            COUNT(CASE WHEN status='404 NOT FOUND' THEN 1 ELSE NULL END)
            AS errorLog, COUNT(*) AS allLog FROM log
            GROUP BY date(time)) AS visits
            WHERE ((errorLog * 1.0/allLog)*100) > 1
            """
    highErrorDay = executeQuery(query)
    print('On which days did more than 1%' + ' of requests lead to errors?')
    for i in highErrorDay:
        print ("{} - {}% errors".format(i[0].strftime('%B %d, %Y'), i[1]))


if __name__ == '__main__':
    print(" ")
    topArticles()
    print(" ")
    topAuthors()
    print(" ")
    errorDays()
    print(" ")
