def drink_me(param):
    msg = 'Выпиваем '+param+' стакан'
    print(msg)
    param = 'пустой'

glass = 'полный'
drink_me(glass)
print('Стакан',glass)


def drink_me_1(param):
    msg = 'Выпиваем '+param+' стакан'
    print(msg)
    param = 'пустой'
    return param

glass_1 = 'полный'
glass_1 = drink_me_1(glass_1)
print('Стакан',glass_1)
