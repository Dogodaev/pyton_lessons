def ask(text):
    ''' Метод вызывает метод проверки на палиндром и выводит итоговый результат'''
    alarm = counter(text)
    if alarm:
        print(text + ' - является палиндромом')
    else:
        print(text + ' - не является палиндромом')

def counter (text):
    ''' Метод проверяет, является ли слово палиндромом'''
    text_revers = text[::-1]
    state = True
    for i in range(len(text)):
        if text[i]!= text_revers[i]:
            state = False
    return state

print('Введите слово для проверки на палиндром.')
print ('Для выхода из программы напишите слово "end"')
num = True
# Этот цикл спрашивает слово для проверки. Работает до написания слова end
while num:
    meaning = input()
    if meaning == 'end':
        num = False
        print('Вы вышли из программы')
    else:
        ask(meaning)
    
