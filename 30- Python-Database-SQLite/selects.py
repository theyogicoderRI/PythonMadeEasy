import sqlite3 
import csv

conn = sqlite3.connect('first_db.db') 
c = conn.cursor()

#select firstname only
c.execute("SELECT fname from people") 
for name in c:
    print("First Name Only ", name)  
    print()

#select firstname and lastname only
c.execute("SELECT fname, lnam from people") 
for name in c:
    print("First namd and Last Name: ", name) 
    print()  

#select firstname and lastname  order by lastname in descending order
c.execute("SELECT fname, lnam from people ORDER BY lnam DESC") 
for name in c:
    print("Order by DESC ", name)    
    print()   

#select firstname and lastname and age  order by lastname in descending and the  age ascending
c.execute("SELECT fname, lnam, age from people ORDER BY lnam DESC, age ASC") 
for name in c:
    print("Order by 2 different Criterion: ", name) 
    print()

#sort by column position
c.execute("SELECT fname, lnam, age from people ORDER BY 3") 
for name in c:
    print("Sort by Position: ", name) 
    print()   

#using Distinct - remove duplicates
c.execute("SELECT DISTINCT fname, lnam FROM people") 
for name in c:
    print("Distinct: ", name)
    print()       

#using Distinct - remove duplicates and then
#remove further dubplicates from the subset and sort in ascending order
c.execute("SELECT DISTINCT fname, lnam FROM people") 
c.execute("SELECT DISTINCT lnam FROM people ORDER BY lnam ASC") 
for name in c:
    print("Compund Distinct: ", name)  
    print()  

# using Where clause
c.execute("SELECT fname, lnam, age FROM people WHERE age > 50") 
for name in c:
    print("Where Clause: ", name) 
    print()   

# where using And
c.execute("SELECT fname, lnam, age FROM people WHERE lnam = 'Jones' AND fname = 'Joey' ") 
for name in c:
    print("Where with And: ", name)
    print()  

# using Limit
c.execute("SELECT fname, lnam, age FROM people  Limit 2 ") 
for name in c:
    print("Using Limit: ", name) 
    print() 

# using Limit and Offset
c.execute("SELECT fname, lnam, age FROM people  Limit 2 OFFSET 5 ") 
for name in c:
    print("Limit and Offset: ", name)  
    print()                            


conn.close()  #close the connection to the db