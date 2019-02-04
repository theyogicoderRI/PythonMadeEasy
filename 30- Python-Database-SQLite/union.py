import sqlite3  

conn = sqlite3.connect('first_db.db') 
c = conn.cursor()

# combines all unique values from each table
print("****Union****\n")
for row in c.execute('''SELECT guit_brand, guit_model FROM guitars UNION SELECT e_guit_brand, e_guit_model FROM e_guitars '''):
    print(list(row))
    
print()
print("****Union All****\n")
# combines all values from each table
for row in c.execute('''SELECT guit_brand, guit_model FROM guitars UNION ALL SELECT e_guit_brand, e_guit_model FROM e_guitars '''):
    print(list(row))  


print("****Union****\n")
for row in c.execute('''SELECT guit_brand, guit_model FROM guitars UNION SELECT e_guit_brand, e_guit_model FROM e_guitars ORDER BY guit_brand '''):
    print(list(row))      
