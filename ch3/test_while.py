# Импортируем модуль random
import random

#Делаем генератор выбора варианта ответа компьютера из предложенных вариантов
random_choice = random.randint(0,101)
print(random_choice)

# создаем счетчик попыток
guesses=0

# Запрашиваем у клиента цвет и считаем попытки, с которой он угадал цвет
while random_choice!=guesses:
    print(guesses)
    guesses = guesses + 1

#Выводим результат в зависимости от кол-ва попыток в корректной форме.
if guesses==1:
    print('Вы угадали цифру ', random_choice, 'за ', guesses, 'попытку')
elif guesses >1 and guesses<5:
    print('Вы угадали цифру ', random_choice, 'за ', guesses, 'попытки')
else: print('Вы угадали цифру ', random_choice, 'за ', guesses, 'попыток')



