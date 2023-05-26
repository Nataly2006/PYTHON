class pet:

    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.ruido = ruido

    # implement the following methods:
    # sleep() - increases the pets energy by 25
class dormir(self):
    def __init__():
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
class alimentar(self):
    def ___init__():
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def jugar(self):
        self.health += 5
        self.energy -= 15
        return self

    # noise() - prints out the pet's sound
    def ruido(self):
        print(self.ruido)


class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.jugar()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Alimentar {self.pet.name} {food}!")
            self.pet.alimentar()
        else:
            print("Oh no!!! se necesita mas comida!")
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.ruido()

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['Pizza','Burger']

Pingüino = pet("Mr. Pingüino","Horse",['Pingüino on things','is invisible'],"Hey Hey")

adrien = Ninja("Adrien","Dion",my_treats,my_pet_food, Pingüino)

adrien.feed()
adrien.feed()
adrien.feed()