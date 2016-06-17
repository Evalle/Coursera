class PartyAnimal:

    x = 0 
    
    def __init__(self):
        print("I'm constructed")

    def party(self):
        self.x += 1
        print("So far", self.x)

    def __del__(self):
        print("I'm destructed", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

print("Type", type(an))
print("Dir", dir(an))
