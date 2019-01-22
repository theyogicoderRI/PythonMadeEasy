# class/Instance creations

class Instruments():
    def __init__ (self, category, name, sound_type ):
        self.category = category
        self.name = name
        self.sound_type = sound_type
        

    def get_category(self):
        return self.category

    def get_name(self):
        return self.name

    def get_sound_type(self):
        return self.sound_type

    def set_category(self, newCat = ''):
        self.category = newCat

    def set_name(self, newName = ''):
        self.name = newName

    def set_sound_type(self, stype = ''):
        self.sound_type= stype

    def __str__ (self):
        return "Insturment:  " +str(self.name) + ":" + str(self.category) + ":" +str(self.sound_type) 
    

##g1 = Instruments("String", "Guitar", "Versatile")
##g2 = Instruments("String", "E-Guitar", "Agressive")
##v1 = Instruments("String", "Violin", "Dynamic")
##print(g1.get_name())
##print("Guitar (g2) at first: ", g2)
##g2.set_name("Electric-Guitar"), g2.set_sound_type("Fuzzy")
##print("Guitar (g2) after changes: ",g2)
##print("Instrument-name: ", g1.get_name(),", Instrument-type: ", g1.get_category())
##print(v1)


# create a subclass of Instruments called Guitars

class Guitars(Instruments):
    Guit_Nums = 1  # created class variable
    
    # instances consructor method
    def __init__ (self,category, name, brand, sound_type,  year, g_type):
        Instruments.__init__(self, category, name, sound_type )
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
        return "This Guitar is a : " +str(self.name)+ "," +str(self.brand)

 
g3 = Guitars("String", "T5", "Taylor","sweet",  "2012", "Accoustic/Electirc")
print(g3)
g4 = Guitars("String", "Jumbo", "Gibson", "booming", "1966", "Accoustic")
print("This Gibson Jumbo is: ", g4.sound_type, ', And was built in: ',  g4.year)
print("How Many Guitars have been created? ", Guitars.Guit_Nums)
print("What is g4's GID? ", g4.gid)
print(g4.g_type)
g4.set_play("Classical")
print(g4.g_type)


##if __name__ == '__main__':
##    
##    g3 = Guitars("String", "T5", "Taylor","sweet",  "2012", "Accoustic/Electirc")
##    print(g3)
##    g4 = Guitars("String", "Jumbo", "Gibson", "booming", "1966", "Accoustic")
##    print("This Gibson Jumbo is: ", g4.sound_type, ', And was built in: ',  g4.year)
##    print("How Many Guitars have been created? ", Guitars.Guit_Nums)
##    print("What is g4's GID? ", g4.gid)
##    print(g4.g_type)
##    g4.set_play("Classical")
##    print(g4.g_type)

    
    
