# Импортируем библиотеку рандома
import random

# Создаем объект с именем bark, который выводит информацию в зависимости от веса собаки
def bark(name, weight):
    if weight > 20:
        print(name, 'говорит ГАВ-ГАВ с весом', weight)
    else:
        print(name, 'говорит гав-гав с весом', weight)

# Вызываем объект bark и передаем ему информацию для обработки
bark('Тузик', 40)
bark('Смайли', 9)
bark('Джейсон', 12)
bark('Филя', 65)
print('')

# Передаем объекту bark список имен собак и генерируем их вес
dogs_name = ['Харон', 'Алсо', 'Чарли', 'Дора', 'Кнопка', 'Рекс', 'Лана', 'Таврис', 'Роза', 'Джейк']
for i in range(len(dogs_name)):
    bark(dogs_name[i],random.randint(5,80))


print('')
print('')
print('')

def get_bark(weight):
    if weight > 20:
        return 'ГАВ-ГАВ'
    else:
        return 'гав-гав'

tuzik_weight = get_bark(40)
print('Тузик говорит',tuzik_weight)
