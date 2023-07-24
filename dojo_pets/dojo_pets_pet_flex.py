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
        print(f'Energy: {self.energy}, Health: {self.health}')
        return self
    
    def play(self):
        self.health += 5
        print(f'Health: {self.health}')
        return self
    
    def noise(self):
        print(self.noise)
        return self


#myers = Pet("Myers", "cat", "fast boi", "meow")
