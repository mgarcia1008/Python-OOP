class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food


    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("You need more pet food")
        return self
    
    def bathe(self):
        self.pet.noise()
        return self


class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        print({self.energy})
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print("Energy: {self.energy}, Health: {self.health}")
        return self
    
    def play(self):
        self.health =+ 5
        print("Health: {self.health}")
        return self
    
    def noise(self):
        print(self.noise)


pet_treats = ["cheese", "greenies", "chews"]
pet_food = ["wet food", "dry food"]

myers = Pet("Myers", "cat", "fast boi", "meow")

mindi = Ninja("Mindi", "Garcia", "myers", "pet_treats", "pet_food")

#mindi.feed()
#mindi.walk()
mindi.bathe()


