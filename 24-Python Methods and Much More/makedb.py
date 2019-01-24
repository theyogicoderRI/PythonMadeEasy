from methodstuff import Employee, Boss
import shelve

test = Employee("Test", "Tester", 10)
test2 = Employee("Test2", "Tester2", 22)
test3 = Boss("Test3", "Tester3", 32)

db = shelve.open('employdb')
for o in (test, test2, test3):
    db[o.fname] = o
db.close()    


# Retrieve data from the shelve :

db = shelve.open('employdb')
print(len(db))

for k in sorted(db):
    print(k, '-', db[k])


