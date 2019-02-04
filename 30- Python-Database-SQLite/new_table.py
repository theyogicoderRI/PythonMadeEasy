import sqlite3  

database = 'first_db.db'

def new_table():
 
    # create a database connection
    conn = sqlite3.connect(database)
    c = conn.cursor()

     # create table 1
    c.execute(""" CREATE TABLE IF NOT EXISTS guitars (
                                        guit_id integer PRIMARY KEY,
                                        guit_brand text NOT NULL,
                                        guit_model text,
                                        guit_price int,
                                        group_id int
                                    ); """)  

     # create table 2
    c.execute(""" CREATE TABLE IF NOT EXISTS e_guitars (
                                        e_guit_id integer PRIMARY KEY,
                                        e_guit_brand text NOT NULL,
                                        e_guit_model text,
                                        e_guit_price int,
                                        group_id integer NOT NULL,
                                        FOREIGN KEY (group_id) REFERENCES guitars(group_id)
                                    ); """)                                  


if __name__ == '__main__':
    new_table()        