from Dog_class import *
from Person_class import *

# Тесты
def dog_test():
    tuzik = Dog('Тузик', 12, 38)
    jackson = Dog('Джексон',9,12)
    print_dog(tuzik)
    print_dog(jackson)
    age = tuzik.human_years()
    print(age)
    print(tuzik)
    print(jackson)
    separator()

def ServiceDog_test():
    rudy = ServiceDog('Руди', 8, 38, 'Джозеф')
    print('Собаку зовут', rudy.name)
    print('Хозяина собаки зовут', rudy.handler)
    print_dog(rudy)
    rudy.is_working = True
    rudy.bark()
    rudy.walk()
    print(rudy)
    separator()

def isinstance_test():
    rudy = ServiceDog('Руди', 8, 38, 'Джозеф')
    if isinstance (rudy, Dog):
        print (True)
    else:
        print(False)
    separator()

def FreesbeeDog_test():
    reks = FreesbeeDog('Рекс', 5, 34)
    red_frisbee = Frisbee('Красный')
    print(reks)
    reks.bark()
    reks.give()
    reks.catch(red_frisbee)
    reks.bark()
    print(reks)
    frisbee = reks.give()
    print(frisbee)
    reks.give()
    print(reks)
    separator()

def Hotel_test_check_dogs():
    tuzik = Dog('Тузик', 12, 38)
    jackson = Dog('Джексон',9,12)
    rudy = ServiceDog('Руди', 8, 38, 'Джозеф')
    reks = FreesbeeDog('Рекс', 5, 34)
    red_frisbee = Frisbee('Красный')
    reks.catch(red_frisbee)
    separator()
    
    hotel = Hotel('Отель "Псины"')
    hotel.check_in(tuzik)
    hotel.check_in(jackson)
    hotel.check_in(rudy)
    hotel.check_in(reks)
    hotel.barktime()
    separator()
    
    hotel.check_out('Рекс')
    hotel.check_out('Пес')
    hotel.check_out('Рекс')

def Hotel_test_walk():
    tuzik = Dog('Тузик', 12, 38)
    jackson = Dog('Джексон',9,12)
    rudy = ServiceDog('Руди', 8, 38, 'Джозеф')
    reks = FreesbeeDog('Рекс', 5, 34)
    red_frisbee = Frisbee('Красный')
    reks.catch(red_frisbee)
    separator()

    tuzik.walk()
    jackson.walk()
    rudy.walk()
    reks.walk()

def Hotel_test_walking_service():
    tuzik = Dog('Тузик', 12, 38)
    jackson = Dog('Джексон',9,12)
    rudy = ServiceDog('Руди', 8, 38, 'Джозеф')
    reks = FreesbeeDog('Рекс', 5, 34)
    separator()
    
    hotel = Hotel('Отель "Псины"')
    hotel.check_in(tuzik)
    hotel.check_in(jackson)
    hotel.check_in(rudy)
    hotel.check_in(reks)
    separator()

    kim = Person('Ким')
    hotel.hire_walker(kim)
    den = DogWalker('Ден')
    hotel.hire_walker(den)
    hotel.walking_service()

def Hotel_test_Person_walking_service():
    tuzik = Dog('Тузик', 12, 38)
    jackson = Dog('Джексон',9,12)
    smiley = Dog('Джексон',9,12)
    rudy = ServiceDog('Руди', 8, 38, 'Джозеф')
    rudy.is_working = True
    jim = FreesbeeDog('Джим', 5, 34)
    separator()
    
    hotel = Hotel('Отель "У пса"')
    hotel.check_in(tuzik)
    hotel.check_in(jackson)
    hotel.check_in(rudy)
    hotel.check_in(jim)
    separator()

    joe = DogWalker('Джо')
    hotel.hire_walker(joe)
    
    hotel.walking_service()
    

def only_name():
    hotel = Hotel('Отель "Псины"')
    reks_1 = FreesbeeDog('Рекс', 5, 34)
    hotel.check_in(reks_1)
    hotel.view()
    reks_2 = FreesbeeDog('Рекс', 2, 17)
    hotel.check_in(reks_2)
    hotel.view()
    hotel.check_out('Рекс')
    
    

#Место вызова
def main():
    #dog_test()
    #FreesbeeDog_test()
    #isinstance_test()
    #Hotel_test_check_dogs()
    #Hotel_test_walk()
    #Hotel_test_walking_service()
    Hotel_test_Person_walking_service()
    #only_name()
    
    separator()

if __name__ == '__main__':
    main()
