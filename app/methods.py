# load the adapter
import psycopg2

# load the psycopg extras module
import psycopg2.extras

class methods():
	def queryFriendCount(id):

		try:
		    conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
		    print("Successful connection to the database!")
		except:
		    print("I am unable to connect to the database")

		cur = conn.cursor()

		try:
			cur.execute('SELECT array_length(friend_id, 1) AS friend_count FROM team3.friends WHERE user_id = %s', (str(id),))
		
		except psycopg2 as e:
  			pass

		results = cur.fetchall()
		return results[0][0]
