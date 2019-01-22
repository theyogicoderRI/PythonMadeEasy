### define an empty tuple
##tup1 = ()
##print(type(tup1))
### output -----> <class 'tuple'>
##
### a one-item tuple
### note: trailing comma is required for single-item tuples
###to disambiguate defining a tuple or an expression surrounded by parentheses
##tup2 = (9,)
##
### a four-item tuple- note: you dont need the "( )" technically
##tup3 = "hi", 1, "hello" , 2
##print(type(tup3))
### output -----> <class 'tuple'>
##
###nested tuple
##tup4 = ("cakes", ("Red Velvet", "German Chocolate"))
##print(tup4)
##
### convert/cast a string to a tuple
##tup5 = tuple('hello')
##print(tup5)
### prints-----> ('h', 'e', 'l', 'l', 'o')
##
### tuple index and slicing
##tup4 = ("cakes", ("Red Velvet", "German Chocolate"))
##print(tup4[0])   #-----> prints 'cakes'
##print(tup4[1][1]) #-----> prints 'German Chocolate'
##
### concatenate
##print(tup5 +tup5 + tup5)
###prints -----> ('h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o')
##
### create a list from a tuple using list comprehension
##tup6 = (25,)
##y = [ x ** 2 for x in tup6]
##print(y)
### prints ----> [625]
##print(type(y))


# named tuple
##from collections import namedtuple
##
##Person_size = namedtuple('Person_size', ['x', 'y'])
##mike = Person_size(6.2, 196)
##print("Mike's Height: ", mike[0])
##print("Mike's Weight: ", mike[1])
##
##
##mary = [5.4, 132]
##mary_H_W = Person_size._make(mary)
##print(mary_H_W)


# How to Sort a tuple
##tup7 = ("Mary", "John", "Liza", "Burt", "Zelda", "Pippa")
##print(sorted(tup7))
### output-----> ['Burt', 'John', 'Liza', 'Mary', 'Pippa', 'Zelda']
##
###index method
##print(tup7.index("Liza"))
###output -----> 2
##
### count method
##tup8 = (1,2,3,1,3,3,4,5,3,3,7,5,6)
##print(tup8.count(3))
###output -----> 5

# convert dictionary values and keys to a tuple:
##dict1 = {"name": "Max", "Age": 10, "Breed": "Coonhound"}
##tup9 = tuple(dict1.values())
##print(tup9)   # output -----> ('Max', 10, 'Coonhound')
##tup10 = tuple(dict1.keys())
##print(tup10)# output -----> ('name', 'Age', 'Breed')
##
### convert dict to a list of tuples
##x1 = list(dict1.items())
##print(x1) # output -----> [('name', 'Max'), ('Age', 10), ('Breed', 'Coonhound')]
##print(type(x1)) # output -----><class 'list'>



coffee = (1.25, 2.15, 4.45, 6.50)
lowest_cost = 0
second_lowest_cost = 0
third_lowest_cost = 0
highest = 0
for x in coffee:
    if x < 2.00:
        lowest_cost = lowest_cost + (30 * x)
    elif x > 2.00  and x < 4.00:  
       second_lowest_cost = second_lowest_cost + (30 * x)
    elif x > 4.00  and x < 6.00:  
       third_lowest_cost = third_lowest_cost + (30 * x)
    else:
        highest = (coffee[3] * 30)     

print("The lowest monthly total for coffee is: ", lowest_cost)
print("The  2nd lowest monthly total for coffee is: ", second_lowest_cost)
print("The  3rd  lowest monthly total for coffee is: ", third_lowest_cost) 
print("The  Highest monthly total for coffee is: ", highest)
print("If I go with the least expensive, compared to the highest, I can save: "\
      , highest - lowest_cost, "at this month's prices")
        
        
        
