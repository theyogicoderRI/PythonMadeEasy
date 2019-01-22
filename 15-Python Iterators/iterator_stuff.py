# using the itertool

##tup = (1 ,2, 3, 4)
##my_it = iter(tup)
##
##print(my_it.__next__())
##print(my_it.__next__())
##print(my_it.__next__())
##print(my_it.__next__())
###print(my_it.__next__()) # no more
##
### plain old for loop:
##tup = (1 ,2, 3, 4)
##for item in tup:
##    print(item)

# list comprehension
##list1 = [1,2,3,4]
##
##mult_list = [i * 4 for i in list1]
##print(mult_list)


# generator expression
list1 = [1,2,3,4]

mult_gen = (i * 4 for i in list1)
##print(type(mult_gen))
##print(next(mult_gen))
##print(next(mult_gen))
##print(next(mult_gen))
##print(next(mult_gen))

#
##for x in mult_gen:
##    print(x)
##
###Generator function
##def one_simple_generator():
##    yield "Happy"
##    yield "Joyous"
##    yield "Free"
##
##for x in one_simple_generator():
##    print(x)


# with a filter

##secret = [10,20,30,40,50]
##def secret_numbers(x):
##    if (x in secret):
##        return x
##    else:
##        return 
##
##my_list = [10,15,20,25,30,35,40]
##x = list(filter(secret_numbers, my_list))
##print(x)

# map() function

##def add_me(val):
##    return val + 100
##
##numbers = (1,2,3)
##map_it = map(add_me, numbers)
##print(set(map_it))

# enumerate() function
##
##yo = ("Yo", "yo there", "yo buddy", "yo yo yo")
##
##for y in enumerate(yo, 1):
##    print(y)


# sorted() function

##my_list1 = ["fish", "monkeys", "zebras", "horses", "camels"]
##
##sort_me =sorted(my_list1, reverse = True)
##print(sort_me)

# any()
##
##my_list = [False, 0, 1, ]
##my_list2 = [False, 0, None, ]
##
##print(any(my_list))
##print(any(my_list2))
##
##
### all()
##
##my_list = [False, 0, 1, ]
##my_list3 = ["Yes", 1, "time", ]
##
##print(all(my_list))
##print(all(my_list3))


# zip()

L1 = [1,2,3,4,5,6]
L2 = [2,3,4,5,6,7]

me_new= dict(zip(L1,L2))
print(me_new)


    
