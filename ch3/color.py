# Импортируем модуль random
import random

#Делаем генератор выбора варианта ответа компьютера из предложенных вариантов
colors = ['синий', 'красный', 'белый']
computer_color = random.choice(colors)
print(computer_color)

# Объявляем переменную для записи в неё цвета пользователя
guess=''

# создаем счетчик попыток
guesses=0

# Запрашиваем у клиента цвет и считаем попытки, с которой он угадал цвет
while guess != computer_color:
    guess = input('Какой цвет я загадал: синий, красный или белый? ')
    guesses = guesses + 1

#Выводим результат в зависимости от кол-ва попыток в корректной форме.
if guesses==1:
    print('Вы угадали цвет ', computer_color, 'за ', guesses, 'попытку')
elif guesses >1 and guesses<5:
    print('Вы угадали цвет ', computer_color, 'за ', guesses, 'попытки')
else: print('Вы угадали цвет ', computer_color, 'за ', guesses, 'попыток')



