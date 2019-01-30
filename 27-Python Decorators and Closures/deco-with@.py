def decorator(func1):
    def wrapper():
        print("This is from the the wrapper function")
        return func1()
    print("This is from the the decorator function")    
    return wrapper # returns wrapper but does not execute - no "( )"

@decorator
def decoratee():
    return 'This is from decoratee Function'   

print(decoratee()) # this executes the wrapper