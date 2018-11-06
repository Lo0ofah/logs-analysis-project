#!/usr/bin/env python3
import psycopg2

DBName = "news"
Question = [
                "What are the most popular three articles of all time?",
                "Who are the most popular article authors of all time?",
                "On which days did more than 1% of requests lead to errors?"
           ]

popularArticles = """SELECT title, count(*) AS numberOfView
                  FROM articles, log
                  WHERE '/article/' || articles.slug = log.path
                  GROUP BY articles.title
                  ORDER BY numberOfView  DESC
                  LIMIT 3;
                  """

popularAuthors = """SELECT name, COUNT(*) AS numberOfView
                 FROM authors, articles, log
                 WHERE authors.id = articles.author
                 AND '/article/' || articles.slug = log.path
                 GROUP BY authors.name
                 ORDER BY numberOfView desc;
                 """
requestErrors = """SELECT day, failurePercent
                 FROM
                 (SELECT allRequest.day,
                 allFailuerRequest.error::double precision
                 /allRequest.request::double precision*100
                 AS failurePercent
                 FROM allRequest, allFailuerRequest
                 WHERE allRequest.day = allFailuerRequest.day
                 ) AS failurePercentage
                 WHERE failurePercent > 1 ;
               """


def executeQuery(query):
        """connect to the database and execute queries
        and return their result """
        db = psycopg2.connect(database=DBName)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result


def PrintPopularArticles(result):
    """format and print the popularArticles query result"""
    for title, numberOfView in result:
        print("\"{}\" _ {} views".format(title, numberOfView))
    print("\n")


def PrintPopularAuthors(result):
    """format and print the popularAuthors query result"""
    for name, numberOfView in result:
        print("{} _ {} views".format(name, numberOfView))
    print("\n")


def PrintRequestErrors(result):
    """format and print the requestErrors query result"""
    for day, failurePercent in result:
        print("{0:%B %d, %Y} _ {1:.1f} % errors".format
              (day, round(failurePercent, 1)))
    print("\n")


def main():
    print("\n")
    print(Question[0])
    resultPopularArticles = executeQuery(popularArticles)
    PrintPopularArticles(resultPopularArticles)

    print(Question[1])
    resultPopularAuthors = executeQuery(popularAuthors)
    PrintPopularAuthors(resultPopularAuthors)

    print(Question[2])
    resultRequestErrors = executeQuery(requestErrors)
    PrintRequestErrors(resultRequestErrors)


if __name__ == '__main__':
    main()
