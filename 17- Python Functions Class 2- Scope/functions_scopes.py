#EXAMPLE #1
##x = 50  # defined in the global scope
##def func(y): # func defined in the global scope
##    z = x + y # y,z local, x is defined in the global scope
##
##    return z
##
##print("Example #1", func(25))
##
##
###EXAMPLE #2
##x = 50  # defined in the global scope
##def func(y): # func defined in the global scope
##    x = 100 # x defined in local to func()
##    z = x + y # y,z local, x is defined in the global scope
##
##    return z
##
##print("Example #2", func(25))
##
##'''When you use an unqualified name inside a function, Python searches up to four scopes in this order:
##L- Local
##E- the local scopes of any enclosing defs (nested functions)
##G- Global
##B-Built-in '''





#without using the global statement in the funcion
##x = 10 # global space
##
##def globs():
##   # no global x
##    x = 100
##    
##    return x
##
##print("2. Calling the function: ", globs())
##print("2. Print x in global space: ", x) # this prints the value of x in the global space



x = 10 # global space
def globs():
    global x
    x = 100
    
    return x

print("1. Calling the function: ", globs())
print("1. Print x in global space: ", x) # prints out value of x in global space, this would print 10 normally, but now 100


    

