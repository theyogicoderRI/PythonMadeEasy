class Employee():
    def __init__(self, fname, lname,  months):
        self.fname = fname
        self.lname = lname
        self.months = months    
        
    def emp_pay(self):
        if self.months < 36:
            self.salary = self.months * 1000
            return self.salary
        else:
            self.salary = self.months * 1200
            return self.salary
        
    def pay_raise(self):
        if self.months < 36:
            increase = .05
            new_sal = self.salary + (increase * self.salary)
            return new_sal
        else:
            increase = .08
            new_sal = self.salary + (increase * self.salary)
            return new_sal    
                   
    def __str__(self):
        return "First name: " +str(self.fname)+ ", Last Name: " +str(self.lname)
                         
if __name__ == '__main__':
    judy = Employee("Judy", "Smith", 35)
    print(judy)
    print("Judy gets paid: ", judy.emp_pay(), "per year")
    snoopy = Employee("Snoopy", "Dog", 60)
    print("Snoopy gets paid: ", snoopy.emp_pay(), "per year")
    print("Judy's new salary is: ", judy.pay_raise())
    print("Snoopy's new salary is: ", snoopy.pay_raise())
       
    print("*" * 50)
    print("Sub Class")


#sub class for the Boss's pay
class Boss(Employee):
    '''the Boss class Augments the pay_raise method'''
    def pay_raise(self):
        bonus = self.months * 100
        new_sal = Employee.pay_raise(self) + bonus
        return new_sal
       
donny = Boss("Don", "Maga", 120)
print(donny)
print("Donny gets paid: ", donny.emp_pay(), "per year")
print("Donny's new salary is: ", donny.pay_raise())

#Introspection Tools 
print("#Introspection Tools ******************************************************")

print("Object donny is associated with the + ", donny.__class__.__name__, " + Class") # prints 'Boss'
print("Object judy is associated with the + ", judy.__class__.__name__, " + Class") # prints 'Employee'
print("Object donny is associated with the + ", donny.__class__.__bases__ , " + Class") # prints '(<class '__main__.Employee'>,) '
print("A List of all of Judy's attributes: ", list(judy.__dict__.keys()))

count = 1
for key in donny.__dict__:
    print("Donny attrbute name {}: '{}' - And Value: '{}'".format( count, key, getattr(donny, key)))
    count += 1
    
# remove dunders for an object to just so attributes
#way #1
print(donny.__dict__.keys())

#way #2
attrsNoDunders = list(name for name in dir(donny) if not name.startswith('__'))
print(attrsNoDunders)


