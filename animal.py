'''
Author: Daryll Osis
Date April 4, 2018
Description:  A simple program that focuses on inheritance. 
'''

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self
    
    def displayHealth(self):
        print("Health is currently:", self.health)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name, 170)

    def fly(self):
        self.health -= 10
        return self


animal1 = Animal("dirtydog", 100)
animal1.walk().walk().walk().run().run().displayHealth()

animal2 = Dog("scooby doo")
animal2.walk().walk().walk().run().run().pet().displayHealth()

animal3 = Dragon("drago")
animal3.walk().walk().walk().run().run().fly().displayHealth()
