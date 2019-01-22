####def times(x,y):
####    return x * y
##
####print(times(35,40))
####
####
####myFunc = times(35,40)
####print(myFunc)
##
####print(times('Boo',10))
##
### EXMPLE #2*****************************
####
####def intersect(seq1, seq2): # define function with two parameters
####    res = []  # define an empty list
####    for x in seq1: # scan sequence 1
####        if x in seq2: # determine if items are in common with seq2
####            res.append(x) # if in common, append to list "res"
####    return res  # return the list back to the caller
##
### the caller
####print(intersect('pizza', 'piazza'))
##
### second caller - pass in a list and a tuple of different lengths
####print(intersect([1,2,3,4], (3,2)))
##
##
##  ###############- SCOPES #################          
### EXMPLE #1*****************************
####
####X = 50 # global scope
####def func(Y): # func is global scope
####    Z = X + Y  # Y and Z are local scope, but X is global
####    
####    return Z
##
####print(func(25))
####
##
##
###################EXAMPLE #2
####
####X = 5
####def func():
####    X = 52
####    return X
####    
##func()
##print(X)
##print(func())
##
##x = 3
##def func2():
##    x = 2
##    return x
##
######### EXAMPLE #3  ########## GLOBAL
##
##x = 10
##
##def global_func():
##    global x
##    x = 100
##
##global_func()
##print(x)
##
##
######### EXAMPLE #4  ########## GLOBAL
##
##y, z = 1, 2
##
##def all_global():
##    global x
##    x = 6
##    x = y + z
##
##
##all_global()
##print(x)

####### EXAMPLE #1  ########## NONLOCAL

##x = 99
##
##def f1():
##    x = 88
##    def f2():
##        print(x)
##    f2()
##f1()

#### EXAMPLE #@ ############## NONLOCAL
##
##def maker(N):
##    def action(X):
##        return X ** N
##    return action
##
##f = maker(2)
##print(f(3))
##g = maker(3)
##print(g(4))
##print(f(3))


#### EXAMPLE #4 ############## NONLOCAL

##def maker(N):
##    return lambda X: X ** N
##
##h = maker(3)
##print(h(4))


### REAL NONLOCAL EXAMPLES #########################
##
##def tester(start):
##    state = start
##    def nested(label):
##        nonlocal state
##        print(label, state)
##        state += 1
##    return nested
##
##F = tester(1) # calling theenclosing function tester with a argument of 1
##print(F('JETS')) # calling tester and passing "JETS" as argument for label
##print(F('KNICKS')) # calling tester and passing "KNICKS" as argument for label


################ ARGUEMENTS #####################
##
##def f(a):
##     a = 99
##
##b = 88
##f(b)
##print(b)



##def example(c):
##    a = c
##    return a
##
##print(example("python"))

##def changer(a,b):  #  the function has two parameters a and b
##    a = 2          # a is set to the value of 2
##    b[0] = 'spam'  # the first position in list "b" is set to "spam"
##
##x = 1             # x is set to 1
##L = [1,2]         # "L" is set to a list of 2 objects, 1 and 2
##changer(x, L)     # the function changer is called with x and L as arguements
##print(x, L)       # then we print the current values of x and L



 
################ *ARGS #####################


def intersect(*args):
    res = []
    for x in args[0]: # evaluate the first sequence
        if x in res: continue   # no duplicates- already in our list?, move on
        for other in args[1:]: #for each of the rest of the sequences (2  through however many)
            if x not in other: break # if objects in the first one not in this one (objects dont match), move on
        else:
            res.append(x) # if there is a match, then add it to the list, 'res'
    return res  # when done with the evaluation of each sequence, return the list to the caller.
    
