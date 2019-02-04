import sqlite3 
import csv


CSV_file = 'db_export_file.csv' 
conn = sqlite3.connect('first_db.db') 

c = conn.cursor()

export_list = []
headers = ["First Name", "Last Name", "Profession", "Age"]

for row in c.execute('SELECT * FROM people ORDER BY age'):
    export_list.append(row)

    with open(CSV_file, 'w') as export:
        writer = csv.writer(export)
        writer.writerow(headers)
        writer.writerows(export_list)
