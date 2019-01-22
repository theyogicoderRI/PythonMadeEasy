# class/Instance creations

class Instruments():
    def __init__ (self, category, name, ):
        self.category = category
        self.name = name
        
    def get_category(self):
        return self.category

    def get_name(self):
        return self.name

    def set_category(self, newCat = ''):
        self.category = newCat

    def set_name(self, newName = ''):
        self.name = newName

    def __str__ (self):
        return "Insturment " +str(self.name) + ":" + str(self.category)

# create a subclass of Instruments called Guitars

class Guitars(Instruments):
    Guit_Nums = 1  # created class variable
    
    # instances consructor method
    def __init__ (self, category, name, brand, year, g_type):
        Instruments.__init__(self, category, name)
        self.brand = brand
        self.year = year
        self.g_type= g_type
        self.gid = Guitars.Guit_Nums   # from class var
        Guitars.Guit_Nums += 1   # increment # of guitars created 

    def set_play(self, style= ""):
        self.g_type = style
        
    def get_gid(self):
        return str(self.gid)    

    def __str__ (self):
        return "This Guitar is a : " +str(self.name)+ ":" +str(self.brand)

if __name__ == '__main__':
    
    g3 = Guitars("String", "T5", "Taylor", "2012", "Accoustic/Electirc")
    print(g3)
    g4 = Guitars("String", "Jumbo", "Gibson", "1966", "Accoustic")
    print(g3)
    print(g4)
    print("How Many Guitars have been created? ", Guitars.Guit_Nums)
    print("What is g4's GID? ", g4.gid)
    print(g4.g_type)
    g4.set_play("Classical")
    print(g4.g_type)



    

    
    
