import psycopg2

DBName = "news"
Question = ["What are the most popular three articles of all time?",
           "Who are the most popular article authors of all time?",
           "On which days did more than 1% of requests lead to errors?"
          ]

def executeQuery(query):
    db = psycopg2.connect(database=DBName)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

firstQuery = """select title, count(*) as numberOfView
                from articles,log
                where articles.slug = substring(log.path, 10)
                group by articles.title
                order by numberOfView  desc
                limit 3;
            """

print(Question[0])
print(executeQuery(firstQuery))
