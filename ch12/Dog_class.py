from Person_class import *

class Dog:
    def __init__ (self, name, age, weight):
        self.name = name
        self.age = age
        self. weight = weight

    def bark (self):
        if self.weight > 29:
            print(self.name, 'лает "ГАВ-ГАВ" ')
        else:
            print(self.name, 'лает "гав-гав" ')

    def walk(self):
        print(self.name, 'на прогулке')

    def human_years(self):
        human_age = self.age*7
        return human_age

    def __str__(self):
        return 'Я собака по имени ' + self.name

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False

    def walk(self):
        if self.is_working:
            print(self.name, 'помогает своему хозяину(' + self.handler + ') ходить')
        else:
            Dog.walk(self)

    def bark(self):
        if self.is_working:
            print(self.name, 'говорит: "не могу лаять, я на работе"')
        else:
            Dog.bark(self)

class Frisbee:
    def __init__(self,color):
        self.color = color

    def __str__(self):
        return 'Я ' + self.color + ' диск-фрисби'

class FreesbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee != None:
            print(self.name, 'говорит: "не могу лаять, я держу фрисби"')
        else:
            Dog.bark(self)

    def walk(self):
        if self.frisbee != None:
            print(self.name, 'говорит: "не могу гулять, я играю с фрисби"')
        else:
            Dog.walk(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'поймал', frisbee.color, 'диск фрисби')

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'отдает', frisbee.color, 'диск фрисби')
            return frisbee
        else:
            print(self.name, 'не держит фрисби')
            return None



    def __str__(self):
        if self.frisbee:
            return 'Я собака по имени ' + self.name +' и у меня есть фрисби'
        else:
            return Dog.__str__(self)
        

class Hotel:
    def __init__(self,name):
        self.name = name
        self.kennel = {}

    def check_in(self,dog):
        if isinstance (dog, Dog):
            self.kennel[dog.name] = dog
            print(dog.name, 'заселился в', self.name)
        else:
            print('Извините,', self.name, 'только для собак')

    def check_out(self, name):
        if name in self.kennel:
            dogs_return = self.kennel[name]
            del self.kennel[name]
            print(name, 'выселился из', self.name)
            return dogs_return
        print('Извините,', name, 'не обнаружен в', self.name)
        return None

    def barktime(self):
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.bark()

    def view(self):
         for dog_name in self.kennel:
             dog = self.kennel[dog_name]
             print(dog.name)

    def hire_walker(self, walker):
        if isinstance(walker, DogWalker):
            self.walkerf = walker
        else:
            print('Извините', walker.name, 'не может выгулливать собак')

    def walking_service(self):
        if self.walkerf != None:
            self.walkerf.walk_the_dogs(self.kennel)

def print_dog(dog):
    print(dog.name + ': возвраст - ', dog.age, ', вес -', dog.weight)

def  separator():
    print('-------------------------------------------------------------')
    
