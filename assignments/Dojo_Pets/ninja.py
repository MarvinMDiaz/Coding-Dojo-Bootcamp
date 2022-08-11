
from pets import Dragon, Pet

class Ninja(Pet):

    def __init__ (self,first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats= treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is walking his {self.pet}")
        
    def feed():
        pass

    def bathe():
        pass




Naruto = Ninja("Naruto","Uzumaki", "Ramen", "Ramen for animals", "9 tails").walk()
# Draco  = Dragon("Draco", "Dragon", "Can Fly", 100, 75).sleep().sleep().eat().play().noise()

