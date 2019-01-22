
##counter = 0
##for i in range(10):
##     print(counter, ": is the number now")
##     counter += 1
##    
##list1 = ["a", "b", "c"]
##for i in list1:
##    print(i, end = ' ')


##
##for i in range(2, 10, 2):
##     print(i , "hi")
  

# with tuples

##tup2 = (("Rosie", "dog", "beautiful"), ("Chihuahua", "black/brown", "killer"))
##print(type(tup2))
##for (x, y, z) in tup2:
##    print("Tuples zero position: ", x)
##    print("Tuples one position: ", y)
##    print("Tuples two position: ", z)


##tup2 = (("Rosie", "dog", "beautiful"), ("Chihuahua", "black/brown", "killer"))
##print(type(tup2))
##for (x) in tup2:
##    print("Print em all together: ", x)
   
##    
##dict1 = {"apple": "1 a day", "pear": "every other day", "peach": "only at the beach"}
##for key, value in dict1.items():
##    print("Just the keys: ",key)
##    print("Just the values: ",value)



list1 = ["peach", "apple", "pear", "mango" , "watermelon"]
list2 = [ "orange", "pear", "mango" , "honeydew", "peach"]

res_list = []
##for item1 in list1:
##    for item2 in list2:
##        if item2 == item1:
##            print(item1, "Is an item in common")
##            res_list.append(item1)
##print(res_list)


##
##for item1 in list1:
##    if item1 in list2:
##        res_list.append(item1)
##    else:
##        print(item1, "was not found")          
##print(res_list)



##my_string = "Python3!Great"
##password = ' '
##rev = my_string[::-1]
##
##for i in range(2):
##    new = rev[i::2] + rev[:i]
##    password = password + new
##    print(i, password, len(password) )
##
##print(password[:13])


rev = "Hello"
password = ' '

for i in range(len(rev)):
    print("Iteration #:",i)
    print("rev[i:] is" , rev[i:])
    print("rev[:i] is" , rev[:i])
    print()
    new = rev[i:] + rev[:i]
    password = password + new    
    
 



