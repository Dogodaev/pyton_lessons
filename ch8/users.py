users = {}
users['Ким'] = {'Эл. почта':'kim@oreolly.com','Пол':'ж','Возвраст': 27,'Друзья':['Джон','Джош']}
users['Джон'] = {'Эл. почта':'john@abc.com','Пол':'м','Возвраст':24,'Друзья':['Ким','Джош']}
users['Джош'] = {'Эл. почта':'josh@wikedlusmart.com','Пол':'м','Возвраст':32,'Друзья':['Ким']}

def average_age(name):
    '''Функция принимает имя пользователя в строковом виде,
проверяет, есть ли он в базе и выводит сообщение о среднем возврасте
друзей пользователя(при их наличии)
'''
    global users
    user = users[name]
    
    if user['Друзья']: # Проверяем, есть ли у пользователя друзья
        friends = user['Друзья'] # Собираем список имен друзей
        age = 0
        
        # В данном цикле проверяем имя каждого друга на наличие в БД
        for name_friends in friends:
            if name_friends in users: # Проверяем, есть ли друг в бд
                friend = users[name_friends]
                age = age + friend['Возвраст']
                
        age = age / len(friends) # Высчитываем средний возвраст друзей пользователя
        print(name,'средний возвраст друзей:', age)

def anti_social():
    global users
    num = 0
    most_anti_social = ''
    
    for name in users:
        user = users[name]
        count_friends = len(user['Друзья'])
        if num > count_friends:
            num = count_friends
        else:
            most_anti_social = name
    print('Самый антисоциальный пользователь -',most_anti_social)
        

'''Поиск друзей'''
# Передаем имена пользователей в строковом виде
average_age('Ким')
average_age('Джон')
average_age('Джош')
anti_social()


