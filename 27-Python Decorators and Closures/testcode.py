

def decorator(func1):
    def wrapper():
        print("This is from the the wrapper function")
        return func1()
    print("This is from the the decorator function")    
    return wrapper # returns wrapper but does not execute - no "( )"

def decoratee():
    return 'This is from decoratee Function'   

d = decorator(decoratee)
#print(d.__name__) # this equals the wrapper function
output = d() # this = wrapper

print(output) # this executes the wrapper