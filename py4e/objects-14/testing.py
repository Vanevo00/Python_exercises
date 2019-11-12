class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
    #  print("So far",self.x)

animal1 = PartyAnimal()
animal1.party()
animal1.party()
animal1.party()
# PartyAnimal.party(animal1)

# print(PartyAnimal)
print(animal1.x)
print(PartyAnimal.x)