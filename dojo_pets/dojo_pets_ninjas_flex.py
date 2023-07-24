from dojo_pets_pet_flex import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        self.pets = []
        self.pets.append(pet)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise
        return self

    def adopt(self, name, type, tricks, noise):
        self.pets.append(Pet(name, type, tricks, noise))



#mindi = Ninja("Mindi", "Garcia", Pet("Myers", "cat", "fast boi", "meow"), "pet_treats", "pet_food")
mindi = Ninja("Mindi", "Garcia", Pet("Myers", "cat", "fast boi", "meow"), "pet_treats", "pet_food")
print(mindi.pet.name)
mindi.adopt("Jackson", "dog", "whines alot", "bark")
mindi.walk()
print(mindi.pets)
print(mindi.pets[1].name)
mindi.feed()
mindi.walk()
mindi.bathe()
