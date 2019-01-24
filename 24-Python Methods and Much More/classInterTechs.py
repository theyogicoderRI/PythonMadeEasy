class Sup:
    def method1(self):
        print( 'This is in Sup.method1')

    def delegate(self):
        self.action() # this expects action() to be created ina SubClass
        
class Inheritor(Sup):
    pass

class Replacer(Sup):
    def method1(self):
        return 'I am in the Replacer.method1'

class Extender(Sup):
    def method1(self):
        print('I am extending Sup at start- Extender.method1')
        Sup.method1(self)
        return 'I am extending Sup at end- Extender.method1'

class Provider(Sup):
    
    def action(self):
        print('I am from the Provder.action()')


##PRINT STATEMENTS
print("*** From Sup (SuperClass) ***")        
x = Sup()
print(x.method1()) # this prints out from Sup

print()
print("*** From Inheritor ***")
z = Inheritor()
print(z.method1()) # this prints out from Sup- with pass Inherits from SuperClass solely

print()
print("*** From Replacer ***")
q =Replacer()
print(q.method1()) # Replaces Super Method completely

print()
print("*** From Extender ***") # extends from SuperClass
aa = Extender()
print(aa.method1())

print()
print("*** From Provider ***")
y = Provider()
print(y.delegate()) # this is a call to a Sup method but prints
#out from Provider because that is where method action() is defined
        
    
