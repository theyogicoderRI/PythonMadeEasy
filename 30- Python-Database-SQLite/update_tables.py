import sqlite3  

conn = sqlite3.connect('first_db.db') 

c = conn.cursor()

c.execute('''UPDATE people SET fname = "Bubba" Where lnam = "Decker" ''')

for row in c.execute('SELECT * FROM people ORDER BY age'):
   print(row) 

conn.commit() # save changes

conn.close()  #close the connection to the db