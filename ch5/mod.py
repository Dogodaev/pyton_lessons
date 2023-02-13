# Запрашиваем информацию у пользователя и возвращаем его выбор
def mod(atribut,default):
    argument = input(atribut +'['+default+']')
    if argument == '':
        argument = default
    print('Вы выбрали', argument)
    return str(argument)

# Вопросы, задаваемые пользователю и дефолтные ответы
atributs = ['Цвет волос ', 'Длина волос ', 'Цвет глаз ', 'Пол ', 'Носит очки ', 'Носит бороду ']
defaults = ['темные', 'короткие', 'голубые', 'женский', 'нет', 'нет']
choice = [] # Список с информацией о выборе пользователя

# Делаем запрос в объект, получаем ответ о выборе пользователя и записываем его в choice
length = len(atributs)
for i in range(length):
    choice.append(mod(atributs[i],defaults[i]))

# Выводим суммируемую информацию о выборе пользователя
for i in range(length):
    print('Ваш выбор:', atributs[i], '-', choice[i])
