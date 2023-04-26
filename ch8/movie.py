movies = []
movie = {}

movie['Название'] ='Forbidden Planet'
movie['Год'] = 1957
movie['Рейтинг'] = '*****'
movie['Год'] =  1956

movies.append(movie)

movie2 = {'Название':'I Was a Neenage Werewolf',' Год':1957,'Рейтинг':'****'}
movie2['Рейтинг'] = '***'

movies.append(movie2)
movies.append({'Название':'Viking Women and the sea Serpent',
               'Год':1957,
               'Рейтинг':'**'})

movies.append({'Название':'Vertigo',
               'Год':1958,
               'Рейтинг':'*****'})

print('Рекомендации фальмов')
print('--------------------')
for movie in movies:
    if len(movie['Рейтинг'])>=4:
        print(movie['Название'], '(' + movie['Рейтинг'] + ')', movie['Год'])


