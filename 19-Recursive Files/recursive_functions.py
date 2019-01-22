# add the values of a list through recursive function
def mysum(L):
    print("Value of L: ", L)
    if not L:
        return 0
    else:
        return  L[0] + mysum(L[1:])

# inital caller   
print(mysum([1,2, 3]))


##
##
##def sum1(a,b,c):
##    if not "":
##        return 0
##    else:
##        return a + b + c
##
##print(sum1(1,2, 3))
        


