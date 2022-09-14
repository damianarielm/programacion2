class Cat:
    def __init__(self, name, weight, owner, sex, hair_color):
        self.name = name
        self.weight = weight
        self.owner = owner
        self.sex = sex
        self.hair_color = hair_color
    def meow(self):
        print(f"{self.name} says 'meow'")
    def play(self, toy):
        print(f"{self.name} is playing with {toy}!")
    def eat(self):
        print(f"{self.name} is eating")
        self.weight += 0.1
