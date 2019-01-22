##def tester(start):
##    state = start # must have this defined here or 'no binding for nonlocal state found"
##    def nested(label):
##        nonlocal state
##        print(label, state)
##        state += 1  # here we change the value of state. We can because it is nonlocal
##        return ("*" * 10) # i do this instead of having "None" print out
##    return nested # if we dont do this we get a "type error"- object is not callable" and nested wont run
##
##teams = tester(1) # this calls the tester function
##print(teams('knicks')) # this string and the rest are passed in for "label" parameter
##print(teams('jets'))
##print(teams('yankees'))

##def f(a):
##    a = 99
##
##b = 88
##f(b)
##print(b)

#example #1
##def f(a):
##    a = 99
##
##print(f(100)) # returns 'none'... no return to print out a
##
###example #2
##def f(a):
##    a = 99
##    return a # this time we return a = 99
##
##print(f(100))
##
###example #3
##def f(a):
##    a = 99
##    
##b = 88
##f(b)
##print(b)
###this doesn;t return anything from the function at all#it just prints out 88 from our variable set "b"

###slide6
##def changer(a, b):
##    a =2
##    b[0] = 'yo'
##    return a, b
##
##x = 1
##y = [1,2]
##z = changer(x,y)
##print(z)


    

###*args
def words(*args):
    return args

words()  # you can pass nothing
print(words("me")) # pass one string
print(words([1,2,3], (4,5,6))) # pass 1 list and 1 tuple


###**args
##def kwords(**kwargs):
##    return kwargs
##
##kwords()  # you can pass nothing
##print(kwords(a='a', b='b')) # 2 keywords

