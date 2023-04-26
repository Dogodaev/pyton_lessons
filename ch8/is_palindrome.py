def is_palindrome (word):
    if len(word)<=1:
        return True
    else:
        if word[0]==word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False

def conclusion(word):
    metod = is_palindrome(word)
    if metod:
        print(word,'палиндром')
    else:
        print(word,'не палиндром')

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
        conclusion(meaning)
    
