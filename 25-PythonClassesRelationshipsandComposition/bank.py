from compo import Person, Teller, Manager

class Customer:
    def __init__(self, name ):
        self.name = name
    def transaction(self, teller):
        print(self.name, " is helped with a transaction from", teller)
    def mortgage(self, manager):
        print(self.name, " is helped with a mortgage from", manager)    

class ATM:
    def giveMoney(self):
        print("Here's some money")
        
class Bank:
    def __init__(self ):
        self.manager = Manager("Joe") #instance of Manager()
        self.teller = Teller("Judy")#instance of Teller()
        self.atm = ATM() # this creates an intsnace of ATM()

    def transaction(self, name):
        customer = Customer(name)#instance of Customer()- with arg "John"
        customer.transaction(self.teller)#passes "Judy" to Customer.transaction()
        self.atm.giveMoney() # this uses the instance to return method()

    def mortgage(self, name):
        customer2 = Customer(name)#instance of Customer()- with arg "Miles"
        customer2.mortgage(self.manager) #passes "Joe" to Customer.mortgage()   

if __name__ == '__main__':        
    b = Bank()
    b.transaction("John")
    b.mortgage("Miles")
 

