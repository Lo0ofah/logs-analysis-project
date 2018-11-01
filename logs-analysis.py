import psycopg2

DBName = "news"

def executeQuery(query):
    db = psycopg2.connect(database=DBName)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

firstQuery = "select * from authors;"
print(executeQuery(firstQuery))
