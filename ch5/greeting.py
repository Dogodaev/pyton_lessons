greeting = 'Приветствую,'
print (greeting) 

def greet (name, message):
    global greeting
    greeting = 'Привет'
    print (greeting , name + ' ! ' , message) 

greet ('Джун' , 'Увидимся !')
print (greeting) 
