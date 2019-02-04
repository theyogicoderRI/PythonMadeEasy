import sqlite3 
import csv

my_db = 'first_db.db'

upload_file = 'bulk_upload.csv' 

SQL_statement = """ INSERT INTO people (fname, lnam, profession, age) 
VALUES (:fname, :lnam, :profession, :age) """


with open(upload_file, 'rt') as upload:
    reader = csv.reader(upload)

    with sqlite3.connect(my_db) as connect:
        c = connect.cursor()
        c.executemany(SQL_statement, reader)