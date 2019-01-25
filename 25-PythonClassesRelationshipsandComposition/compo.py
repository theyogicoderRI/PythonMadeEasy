class Person:
    def __init__(self, name, salary= 0):
        self.name = name
        self.salary = salary
    def __str__(self):
        return str(self.name) + ' $' +  str(self.salary)

class Teller(Person):
    '''for tellers only!'''
    def __init__(self, name):
        Person.__init__(self, name, 14500)
        self.name = name
  
class Manager(Person):
    '''for mangers only!'''
    def __init__(self, name):
        Person.__init__(self, name, 54500)
        self.name = name    
    
if __name__ == '__main__':
    x = Person("Bob")
    print(x)
    y = Teller("Bill")
    print(y)
    z = Manager("Sally")
    print(z)
