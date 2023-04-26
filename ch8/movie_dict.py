movies = {}
movie = {}

movie['Название'] ='Forbidden Planet'
movie['Год'] = 1957
movie['Рейтинг'] = '*****'
movie['Год'] =  1956

movies['Forbidden Planet'] = movie

movie2 = {'Название':'I Was a Teenage Werewolf','Год':1957,'Рейтинг':'****'}
movie2['Рейтинг'] = '***'

movies[movie2['Название']] = movie2

movies['Viking Women and the sea Serpent']= {'Название':'Viking Women and the sea Serpent',
                                             'Год':1957,
                                             'Рейтинг':'**'}

movies['Vertigo'] = {'Название':'Vertigo',
               'Год':1958,
               'Рейтинг':'*****'}

print('Рекомендации фильмов')
print('--------------------')
for name in movies:
    movie = movies[name]
    if len(movie['Рейтинг'])>=4:
        print(movie['Название'], '(' + movie['Рейтинг'] + ')', movie['Год'])

print()
print('Выбор редакции')
print('--------------------')
movie = movies['I Was a Teenage Werewolf']
print(movie['Название'], '(' + movie['Рейтинг'] + ')', movie['Год'])
