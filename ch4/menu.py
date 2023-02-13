menu = []
menu.append('Бургер')
menu.append('Суши')
print(menu)

del menu[0]
print(menu)

menu.extend(['Барберю','Тако'])
print(menu)

mastery = ['секрет'] * 5
print(mastery)
mastery1 = 'секрет' * 5
print(mastery1)

menu.insert(1, 'Рагу')
print(menu)
