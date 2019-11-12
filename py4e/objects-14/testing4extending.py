from testing3class import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

vojta = PartyAnimal("Vojta")
vojta.party()
klara = CricketFan("Klara")
klara.party()
klara.six()
print(dir(klara))