#property decorator
class Prop():
    def __init__(self, num):
        self.n = num  

    @property
    def propdeco(self): # gets value
        '''I am the doc for prop'''
        return self.n

    @propdeco.setter
    def propdeco(self, value): # sets a value
        print('set num: ', value)
        self.n = value 

    @propdeco.deleter
    def propdeco(self): # deletes a value
        print("deleting num")
        del self.n
      
num = Prop(22)
print("here is the getter: ", num.propdeco)
num.propdeco = 47
print("I just used the setter", num.propdeco)
print(num.__dict__.values())
del num.propdeco
print("And after I used the deleter, the value is gone: ", num.__dict__.values())
