#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

# load the adapter
import psycopg2

# load the psycopg extras module
import psycopg2.extras

try:
    conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
except:
    print("I am unable to connect to the database")

# If we are accessing the rows via column name instead of position we 
# need to add the arguments to conn.cursor.

#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur = conn.cursor()
try:
    cur.execute('SELECT * FROM test;')
    #cur.execute('DROP TABLE foobar;')
    #cur.execute('CREATE TABLE team3.test (id serial PRIMARY KEY, num integer, data varchar);')
    #cur.execute("INSERT INTO test (num, data) VALUES (100, \'testing\');")
    #conn.commit()
    
except psycopg2 as e:
    pass

rows = cur.fetchall()
print("sample rows: ", rows)
print("\nRows: \n")
for row in rows:
    print("id: ", row[1], "\nmovie: ", row [2])
