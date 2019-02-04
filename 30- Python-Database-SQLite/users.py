import sqlite3  

database = 'first_db.db'

def new_table():
 
    # create a database connection
    conn = sqlite3.connect(database)
    c = conn.cursor()

     # create table 1
    c.execute(""" CREATE TABLE IF NOT EXISTS users (
                                        user_id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text CHECK(length(password) >= 8)); """) 

if __name__ == '__main__':
    new_table()                                          