import sqlite3  # import the sqlite to use it

conn = sqlite3.connect('first_db.db') # create a db using the connection method

c = conn.cursor()  # enables you to perform SQL commands

#c.execute('''CREATE TABLE people
        #(fname text, lnam text, profession text, age int )''')  # create table 'people'

#c.execute("INSERT INTO people VALUES ('Mary', 'Lou', 'Teacher', '37')")   
# 
# many_people = [('Bob', 'Barker', 'Banker', '56'),
#              ('Sally', 'Sunshine', 'Seller', '32'),
#              ('Joey', 'Jones', 'Jewler', '44'),]  

# c.executemany("INSERT INTO people VALUES (?,?,?,?)", many_people) 

# many_guitars = [('1', 'Taylor', 'T5', '2000', '1'),
#              ('2', 'Martin', 'HD-28', '3000', '2'),
#              ('3', 'Santa Cruz', '1934 OM', '19000', '3'),
#              ('4', 'Gibson', 'Jumbo', '6000', '5'),]  

# c.executemany("INSERT INTO guitars VALUES (?,?,?,?,?)", many_guitars) 

# many_e_guitars = [('1', 'PRS', 'Custom 22', '2000', '4'),
#              ('2', 'Gibson', 'Les Paul', '3000', '5'),
#              ('3', 'Fender', 'Stratocaster', '3700', '6'),
#               ('4', 'Taylor', 'T5', '2000', '1') ]  

# many_e_guitars = [('5', 'Guild', 'F-512E', '4100', '7'),
#              ('6', 'Fender', 'Acoustasonic', '2000', '6'),
#              ('7', 'Taylor', '814cs', '3900', '1'),
#               ('8', 'Ibanez', 'AW54ce', '300', '8') ] 

# many_guitars = [('5', 'Guild', 'F-512E', '4100', '7'),
#              ('6', 'Fender', 'Acoustasonic', '2000', '6'),
#              ('7', 'Taylor', '814cs', '3900', '1'),
#               ('8', 'Ibanez', 'AW54ce', '300', '8') ] 

# many_guitars = [('9', 'Acara', 'D1', '5200', '9'),
#              ('10', 'Blackbird', 'Savoy', '2500', '10'),
#              ('11', 'Bourgeous', 'D Generation', '3000', '11'),
#               ('12', 'Collings', 'o Braz & Germ', '8800', '12') ] 

# c.executemany("INSERT INTO e_guitars VALUES (?,?,?,?, ?)", many_e_guitars)
# c.executemany("INSERT INTO guitars VALUES (?,?,?,?,?)", many_guitars)  

#c.execute("INSERT INTO e_guitars VALUES ('4', 'Taylor', 'T5', '2000')") 



# many_employees = [('1', 'Joe', 'Johns',  '1'),
#              ('2', 'Gene', 'Rubbermann',  '2'),
#              ('3', 'Barb', 'Simmons',  '2'),
#               ('4', 'Brain', 'Criola',  '3'),
#               ('5', 'Sally', 'Stubbings', '4'),
#              ('6', 'Julie', 'Jones', '1'),
#              ('7', 'Julio', 'Cullio', '1'),
#               ('8', 'Maria', 'Matteo',  '3') ] 

# many_roles = [('1', 'Manager',  '1'),
#              ('2', 'IT',  '2'),
#              ('3', 'Accounting', '3'),
#               ('4', 'Development',  '4') ] 

# many_employees = [
#              ('12', 'Sally', 'Stubbings', '5'),
#              ('13', 'Sally', 'Stubbings', '2'),
#              ('14', 'Maria', 'Matteo',  '5') ,
#              ('15', 'Julio', 'Cullio', '5'),
#               ] 


# c.executemany("INSERT INTO employees VALUES (?,?,?,?)", many_employees)

#c.execute("INSERT INTO roles VALUES ('5', 'Facilities', '5')")   
# for row in c.execute('SELECT  emp_fname, emp_lname, role FROM employees \
# INNER JOIN roles ON roles.num = employees.num'):
#     print(list(row))
# #   
# 
# for row in c.execute('SELECT * FROM employees'):
#     print('Employee: ', row)

# for row in c.execute('SELECT * FROM roles'):
#     print('Roles: ', row)   

# for row in c.execute('SELECT  guit_brand, e_guit_brand FROM guitars \
# CROSS JOIN e_guitars ORDER_BY e_guitars.group_id'):
#     print(list(row))

# for row in c.execute('SELECT  * FROM guitars CROSS JOIN e_guitars'):
#     print(list(row))

# print("*" * 80)
# for row in c.execute('SELECT * FROM people ORDER BY age'):
#    print(row)        
# c.execute('select * from people')
# fetch = c.fetchone()
# fetch2 = c.fetchone()
# fetch3 = c.fetchone()
# print(fetch)
# print(fetch2)
# print(fetch3)

#c.execute("DELETE FROM people WHERE age = 'age' ")  

# export_list = []

# for row in c.execute('SELECT * FROM people ORDER BY age'):
#     #print(row) 
#     export_list.append(row)


# for row in c.execute('SELECT lnam, COUNT(fname) FROM people GROUP BY lnam'):
#     print(list(row) )

# print()

# for row in c.execute('SELECT emp_fname, emp_lname, min(num), max(num), round(avg(num),1) FROM employees GROUP BY  \
#         emp_lname HAVING COUNT(num) > 1'):
#     print(list(row)) 

# c.execute("DELETE FROM employees WHERE emp_lname = 'Criola' ")  

# for row in c.execute('SELECT * FROM employees'):
#         print(list(row))

#rename a table
#c.execute("ALTER TABLE tasks RENAME TO new_tasks  ")  

# add column to exisiting table
#c.execute("ALTER TABLE new_tasks ADD COLUMN effort_level text ")


# add column to exisiting table and include a CHECK constraint
#c.execute("ALTER TABLE users ADD COLUMN password text  \
                    #CHECK(length(password) <= 8)  ")

# insert record, but the password does not meet the check constraint
# c.execute("INSERT INTO users VALUES ('1', 'jsmith', 'hello12')") 


# insert record, but the password does meet the check constraint
# c.execute("INSERT INTO users VALUES ('1', 'jsmith', 'y7eg3yw7h2')") 

conn.commit() # save changes

conn.close()  #close the connection to the db