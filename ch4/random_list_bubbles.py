import random

scores= []
costs=[]
num = 100
k=0
while k< num:
    scores.append(random.randint(40,80))
    costs.append(random.randint(20,40))
    k=k+1

#length = len(scores)
#print(length)
#for i in range(length):
#    print('Позиция №' + str(i), '- имеет значение:',scores[i])



# Объявляем список данных scores
#scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

# Объявляем список цен на растворы costs
#costs = [ 0.25, 0.27, 0.25, 0.25, 0.25, 0.25, 0.33, 0.31, 0.25, 0.29, 0.27, 0.22, 0.31, 0.25, 0.25, 0.33, 0.21, 0.25, 0.25, 0.25, 0.28, 0.25, 0.24, 0.22, 0.20, 0.25, 0.30, 0.25, 0.24, 0.25, 0.25, 0.25, 0.27, 0.25, 0.26, 0.29]

# Находим длину списка scores
length = len(scores)

# Перебираем список scores с выводом его значений
#i=0
#while i<count_tests:
#    print('Пузырьковый раствор №' + str(i), '- результат:',scores[i])
#    i=i+1

for i in range(length):
    print('Пузырьковый раствор №' + str(i), '- результат:',scores[i], 'цена:', costs[i])

# Выводим информацию о кол-ве позиций в списке scores
print ('Пузырьковых тестов:', length)

# Находим наибольшее значение в списке scores и выводим его
high_score = 0
for i in range(length):
    if scores[i]>high_score:
        high_score=scores[i]
print('Наибольший результат:', high_score)

# Находим номера с наибольшим значением в списке scores
best_solutions = []
for i in range(length):
    if scores[i]==high_score:
        best_solutions.append(i)
print('Растворы с наибольшим результатом:', best_solutions)

# Находим максимальную цену в списке costs
high_cost = 0
for i in range(length):
    if costs[i]> high_cost:
        high_cost=costs[i]

# Находим самый выгодный раствор
cost = high_cost
most_effective = 0
for i in range(length):
    if scores[i]==high_score and costs[i]<cost:
        cost = costs[i]
        most_effective = i
print('Раствор', most_effective, 'самый выгодный. Его цена -', cost)
