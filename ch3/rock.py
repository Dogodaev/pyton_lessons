# Импортируем модуль random
import random

# Объявляем переменную для записи в неё победителя
winner = ''

#Делаем генератор выбора варианта ответа компьютера и заменяем его на строковый ответ
random_choice = random.randint(0,2)
computer_choice = ''
user_choice = ''
if random_choice == 0:
    computer_choice = 'камень'
elif random_choice == 1:
    computer_choice = 'бумага'
else:
    computer_choice = 'ножницы'

# Цикл проверки корректного ввода пользователем варианта ответа
while (user_choice != 'камень' and
       user_choice != 'бумага' and
       user_choice != 'ножницы'):
    # Запрашиваем у пользователя его выбор
    user_choice = input('камень, ножницы, бумага ')

# Определяем победителя по логике: ничья, выиграл компьютер, иначе выиграл пользователь
if computer_choice == user_choice:
    winner = 'Ничья'
elif ((computer_choice =='бумага' and user_choice == 'камень') or
      (computer_choice =='камень' and user_choice == 'ножницы')or
      (computer_choice =='ножницы' and user_choice == 'бумага')):
    winner = 'Компьютер'
else: winner = 'Пользователь'

# Выводим информацию о победителе на экран
if winner == 'Ничья':
    print(winner, 'что ж пожелать. Давай сыграем еще раз')
else:
    print(winner,'выиграл, я выбрал,',user_choice,'компьютер выбрал',computer_choice)
