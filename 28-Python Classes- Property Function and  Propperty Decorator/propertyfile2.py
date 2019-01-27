#property function
class Prop():
    def __init__(self, num):
        self.n = num  # this makes the calls to setter, getter and deleter
    
    def getnum(self): # gets value
        '''I am the doc for prop'''
        return self.n

    def setnum(self, value): # sets a value
        print('set num: ', value)
        self.n = value  # this sets the attribute

    def delnum(self): # deletes a value
        print("deleting num")
        del self.n
                
    num = property(getnum, setnum, delnum  ) # this is our property object  called "num"

x = Prop(8) # create an instance for Prop, pass value of 8
print("The getter, returns the value", x.num)  # prints value of self.n
x.num = 124 # this invokes the setter
print(x.__dict__.values()) #before delete prints dict_values([124])
del x.num  # this deletes using delnum
print(x.__dict__.values()) #after del prints dict_values([]) # now empty
print(Prop.num.__doc__)  # get the docstring from property function (4th arguments) or from getnum




    #getnum gets data
    # setnum sets data
    #delnum deletes data
    # num provides an interace to our our values stored in in self.n
    # any code that accesses "num" will be be automatically accessing self.n
    # any code that retrieves the value of "num", will be automatically calling getnum (this
    #happens coutersy of the property function.)
    #same holds true for any code that sets num- will be calling
    #setnum and deleting num will automatically









