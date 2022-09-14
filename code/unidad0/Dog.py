class Dog(Pet):
    def woof(self):
        print(f"{self.name} says 'woof'")

    def eat(self):
        print(f"{self.name} is eating")
        self.weight += 0.2
