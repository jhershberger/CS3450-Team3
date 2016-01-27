import psycopg2
from imdbpie import Imdb
import random
imdb = Imdb()
imdb = Imdb(anonymize=True)
variable = imdb.search_for_title("The Dark Knight")[0]
# conn = psycopg2.connect()
# cur = conn.cursor()
title = imdb.get_title_by_id("tt0468569")
print (title.title)
print (title.rating)
print (title.runtime)
x = 0
listOfPopularMovies = imdb.top_250()
while x<15:
    temp = random.randint(1, 249)
    t = listOfPopularMovies[temp]
    tid = t["tconst"]
    print (tid)
    print (t["title"] + " is the " + str(temp) +"th rated movie")
    print ("It's score is: " + str(t["rating"]))

    x = x + 1
