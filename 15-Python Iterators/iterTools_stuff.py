###itertools
####from itertools import *
##
### create a new iterator
###syntax: iterttols.count(start,step)
##
###this would go on forever
####x = count(10)
####for i in x:
####    print(x)
##
### but done this way
### it would start at 2, end at but dont include 10
##
####for num in islice(count(), 2, 10):
####    print(num, end = " ")
##
### cycle
####count = 0
####for x in cycle([1,2,3,4,5]):
####    count  += 1
####    if count == 25:
####        break
####    print(x, end = ' ')
##
###repeat
####def my_func(x):
####      return x+x
####my_set = {'a', 'b', 'c'}
####
####for x in repeat (my_func(2), 6):
####    print(x, end = ' ')
##   
##### chain()
####list1 = [1,2,3]
####tup1 = (2,3,4)
####set1 = {"a", "b", "c"}
####for x in chain(list1, tup1, set1):
####    print(x, end = ' ')
##
###islice()
##
####list1 = [1,2,3,4,5,6,7,8,9]
####for x in islice(list1, 1, 9, 2):
####    print(x)
##
### accumulate()
####from itertools import *
####from operator import *
#####find the max value
####list1 = [2,1,4,6,8,10,2,4,6,7,9,11,23,4]
####x = list(accumulate(list1, max))
####print(x)
### output: [2, 2, 4, 6, 8, 10, 10, 10, 10, 10, 10, 11, 23, 23]
##
###find the min value
####list1 = [2,1,4,6,8,10,2,4,6,7,9,11,23,4]
####x = list(accumulate(list1, min))
####print(x)
##### output: [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
####
##### find the running product mul standard for multiply
##### from operator.mul package
####nums = [2.5, 1.75, 4.0, 12.25]
####x = list(accumulate(nums, mul))
####print(x)
##### output: [2.5, 4.375, 17.5, 214.375]
####
##### subtract each number of the list from the one before
##### from operator.sub package
####nums = [1,3,4,5]
####x = list(accumulate(nums, sub))
####print(x)
##### output: [1, -2, -6, -11]
####
##### concatenate each number of the list to one after it
##### from operator.concat package
####ani = ["cat", "-fish", "-frogs", "-clams", "-rooster"]
####x = list(accumulate(ani, concat))
####print(x)
###Output: ['cat', 'cat-fish', 'cat-fish-frogs', 'cat-fish-frogs-clams', 'cat-fish-frogs-clams-rooster']

# can do Amortization
# Amortize a 2.5% loan of 3000 with 12 annual payments of 100\
##from itertools import *
##payments = [10000, -261, -261, -261, -261, -261, -261, -261, -261, -261, -261,
##            -261, -261, -261]          
##amor = list(accumulate(payments, lambda bal, pmt: bal * 1.025 + pmt))
##payment = 0
##for pay in amor:
##    print("Payment Number: ", payment, "Loan Amt.: ", pay)
##    payment += 1      


## # tee
##from itertools import *
##my_list = ["a", "b", "c", "d"]
##screen, file1 = tee(my_list)
##
##for i in screen:
##    print( "To the Screen: ", i)
##my_file = open("my_file.txt", "w")    
##for i in file1:
##    print ( "To The File", i, file =my_file)
##my_file.close()

#startmap
from itertools import *
##
##def fun():
##    my_list = ['a', 'b', 'c', 'd']
##    return my_list
##    
##tup1 = ((1, 2),(2,3),(3,4))
##
##
##for i in starmap(fun(), tup1):
##    print(i, end = ' ')

##from itertools import *
##
##values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
##for i in starmap(lambda x,y:(x, y, x*y), values):
##    print(i)
##import os
##my_tup = [("/dir_1", "file1"),("/dir_2", "file2"), ("/dir_3", "file3")]
##x = starmap(os.path.join, my_tup)
##                  
##for i in x:
##    print(i)

# filterfalse()
##from itertools import *
##
##def less_than_20(x):
##    return x < 20
##
##my_list = [1,3,5,6,10,20,30,40]
##my_filt_false = filterfalse(less_than_20, my_list)
##
##for x in my_filt_false:
##    print(x)

##from itertools import *
##
##def less_than_20(x):
##    return x < 20    
##
##my_filt_false = takewhile(less_than_20, count())
##
##for x in my_filt_false:
##    print(x, end = ' ')

##from itertools import *
##
##def less_than_20(x):
##    return x < 20    
##
##my_list = [1,5,6,7,8,18,19,20,21,22,23]
##my_drop = dropwhile(less_than_20, my_list )
##
##for x in my_drop:
##    print(x, end = ' ')

##from itertools import *
##
##list1 = [1,2,3,4,5,6,7]
##list2 = [0,0,0,1,1,1,0]
##
##my_comp = compress(list1, list2)
##for x in my_comp:
##    print(x, end = ' ')

##
##from itertools import *
##
##list1 = [1,2,3,4]
##x = combinations(list1, 2)
##
##for i in x:
##    print(i, end= ' ')
##
##
##
##from itertools import *
##
##list1 = [1,2,3,4]
##x =permutations(list1)
##
##for i in x:
##    print(i, end= ' ')


    
##from itertools import *
##
##list1 = [1,2,3,4]
##x =combinations_with_replacement(list1, 2)
##
##for i in x:
##    print(i, )

## groupby()


from itertools import zip_longest
for i in zip_longest([1,2,3,4], ["a", "b", "c"],'4567', 'hello'):
   print (i)

