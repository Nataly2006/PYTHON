class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def show_info(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nHappiness: {self.happiness}\n")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=80)
        self.roar_level = 5

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=80, happiness=90)
        self.jump_height = 3

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=70, happiness=70)
        self.hibernation_period = "Winter"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all_animals(self):
        for animal in self.animals:
            animal.show_info()


# Ejemplo de uso:

lion = Lion("Kobu", 5)
tiger = Tiger("Kurama", 3)
bear = Bear("Shikamaru", 7)

zoo = Zoo()
zoo.add_animal(lion)
zoo.add_animal(tiger)
zoo.add_animal(bear)

zoo.show_all_animals()

lion.feed()
tiger.feed()

zoo.show_all_animals()