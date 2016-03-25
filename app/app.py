# import the Flask class from the flask module
from flask import Flask, render_template,request

import json
import requests

# load the adapter
import psycopg2

# load the psycopg extras module
import psycopg2.extras

try:
    conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
    print("Successful connection to the database!")
except:
    print("I am unable to connect to the database")

# create the application object
app = Flask(__name__)
print ("app: ", app)

@app.route('/')
def index():
    return render_template('index.html')  # render the index template

@app.route('/nav')
def nav():
    return render_template('nav.html')  # render the navbar template

@app.route('/testSERVER', methods=['POST'])
def testSERVER():
	id = request.form['var']
	print("id: ", id)

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
	return json.dumps({'status':'OK', 'id': rows[2][0], 'movie': rows[int(id)][2]})

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
