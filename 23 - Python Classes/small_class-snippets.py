class Person():
    def __init__(self, name):
        self.n = name

    def __str__(self):
        return "The name is: " + str(self.n)

p1 = Person("Joe")
p2 = Person("Betty")
print(p1)
print(p2)
