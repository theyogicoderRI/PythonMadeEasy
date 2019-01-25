class ABC:
    def mymethod(self):
        self.__word = "Hello"
    def printme(self):
        print(self.__word)

class DEF:
    def mymethod2(self):
        self.__word = "Hi There"
    def printme2(self):
        print(self.__word)

class Sub(ABC, DEF):
    print("I am the sub class")


caller = Sub()
caller.mymethod()
caller.printme()
print(caller.__dict__) # {'_ABC__word': 'Hello'}

caller.mymethod2()
caller.printme2()
print(caller.__dict__) # {'_ABC__word': 'Hello', '_DEF__word': 'Hi There'}

    
    
