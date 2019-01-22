
#our first lambda
##y = lambda x : x + x
##print(y(2))

# output 4


##
##list1 = [lambda w: w  + 'man',
##         lambda w: w  + 'Fan',
##         lambda w: w  + 'Duper',
##         lambda w: w  + 'Smart']
##
##w = "Super"
##
##for item in list1:
##    print(item(w))


##
##def dig():
##    num1 = 2
##    expo = lambda  num2 : (num1 ** num2) // 2
##    return expo
##
##a = dig()
##b = a(4)
##print(b)
##
###output = 8


#convential function mult 2 numbers
##def mult(a,b):
##    return a * b
##
##caller = mult(4,5)
##print(caller)
###output = 20
##
###now using a lambda expression
##c = lambda a, b : a * b
##print(c(4,5))
###output = 20
    
#map function and lambda

##l1 = [2,2,2]  # list 1
##l2 = [5,10,20]  # list 2
##
##tot = map(lambda a,b: a* b, l1, l2) # map using lambda
##print(tot) # this prints out a map object '<map object at 0x10b65d3c8>'
##print(type(tot)) # <class 'map'>
##list_tot = list(tot) # convert tot into type list
##print(list_tot) # print out list  output: [10, 20, 40]

##list3 = [2,4,6,8,10,20,25,30]
##x = filter(lambda x: x > 10, list3)
##for item in x:
##    print(item, end =  ' ')
##
## # output: 20 25 30

animals = [('rosie', 13, "Chihuahua"),
               ('max', 11, "Coonhound"),
               ('Jake', 12, "Border Collie"),]

a = sorted(animals, key=lambda x: x[1], reverse=True)
for x in a:
    print(x)

           
    
