from Dog_class import *

class Person():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я человек по имени ' + self.name

class DogWalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def walk_the_dogs(self,dogs):
        for dog_name in dogs:
            dogs[dog_name].walk()

    
