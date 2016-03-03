import psycopg2
from imdbpie import Imdb
import rtsimple as rt
import random


imdb = Imdb()
imdb = Imdb(anonymize=True)

try:
    conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
except:
    print ("I am unable to connect to the database")
cur = conn.cursor()
x = 0
listofMovies = []
listOfPopularMovies = imdb.top_250()
for x in range(0,5):
    temp = random.randint(1, 249)
    t = listOfPopularMovies[temp]
    tid = t["tconst"]
    print ("Found a random movie from the Top 250:")
    print ("The id used to access this movie is " + tid)
    title = imdb.get_title_by_id(tid)
    print (t["title"] + " is the " + str(temp) +"th rated movie")
    print ("It's score is: " + str(t["rating"]))
    print (str(title.directors_summary[0].name) + " is the director")
    print (str(title.cast_summary[0].name) + " is a big actor in it")
    print ("List of top actors: ")
    newList = []
    for x in range(0,3):
        newList.append(title.cast_summary[x].name)
    for x in range(0,3):
        if x == 2:
            print (newList[x])
        else:
            print (newList[x] + ", ")
    print ("\n")
    listofMovies.append(t["title"])
print (listofMovies)
for n in listofMovies:
    # print (n)
    cur.execute("INSERT INTO test (data) VALUES (%s)", [n])
    conn.commit()
    cur.execute("""SELECT * from test""")
    rows = cur.fetchall()
print ("\nShow me the database before deletion:\n")
for row in rows:
    print ("  k ", row)
for n in listofMovies:
    # print (n)
    cur.execute("DELETE FROM test")
    conn.commit()
    cur.execute("""SELECT * from test""")
    rows = cur.fetchall()
print ("\nShow me the database after deletion:\n")
for row in rows:
    print ("  k ", row)
