import psycopg2

DBName = "news"
Question = ["What are the most popular three articles of all time?",
           "Who are the most popular article authors of all time?",
           "On which days did more than 1% of requests lead to errors?"
          ]

firstQuery = """select title, count(*) as numberOfView
                from articles,log
                where articles.slug = substring(log.path, 10)
                group by articles.title
                order by numberOfView  desc
                limit 3;
            """

secondQuery = """select name , count(*) as numberOfView
                 from authors, articles, log
                 where authors.id = articles.author
                 and articles.slug = substring(log.path, 10)
                 group by authors.name
                 order by numberOfView desc;
              """

def executeQuery(query):
    db = psycopg2.connect(database=DBName)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

def formatFirstQuery(result):
    for title , numberOfView in result:
        print("\"{}\" _ {} views".format( title , numberOfView))
    print("\n")

def formatSecondQuery(result):
    for name , numberOfView in result:
        print("{} _ {} views".format( name , numberOfView))
    print("\n")

print("\n")
print(Question[0])
resultFirstQuery = executeQuery(firstQuery)
formatFirstQuery(resultFirstQuery)

print(Question[1])
resultSecondQuery = executeQuery(secondQuery)
formatSecondQuery(resultSecondQuery)
