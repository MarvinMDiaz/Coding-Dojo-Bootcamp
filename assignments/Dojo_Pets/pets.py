class Pet:



    def __init__ ( self,name, pet_type, tricks, health=100, energy=100):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = health 
        self.energy = energy

    def sleep(self):
        self.energy += 25
        # print(f"Hello {self.name} your energy has gone up, it is now at {self.energy}")
        # return self
            

    def eat(self):
        self.energy += 5
        self.health += 10
        # print(f"Hello {self.name},  your energy is now {self.energy} and your health is now {self.health} ")
        # return self
    def play(self):
        self.health += 5
        # print(f"Aww, {self.name} is playing & its health is now {self.health}")
        return self
        

    def noise(self):
        print (f"The pet makes noise\n")


class Dragon(Pet): 
    def sleep(self):
        super().sleep()
        return self

    def eat(self):
        super().eat()
        return self

    def play(self):
        super().play()
        return self
        

    def noise(self):
        print (f" {self.name} ROOOOAAAAARRRRS\n")


# Draco  = Dragon("Draco", "Dragon", "Can Fly", 100, 75).sleep().sleep().eat().play().noise()


