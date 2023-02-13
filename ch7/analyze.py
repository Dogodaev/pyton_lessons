''' В модуле analyze вычисляется индекс удобочитаемости  Флеша-Кинкей
для заданного текста и на основе полученной оценки определяется уровень
удобочитаемости
'''
# объявляем фукнкцию расчета параметров формулы (функция по вызову функций)
def computer_readavility(text):
    ''' Эта функция основная. Она получает исследуемый текст. В ней происходит
объявления переменных, расчитываемых в формуле,их вычисления посредством
вызова других функций и вызова метода предоставления конечной информации
'''
    # Объявляем переменные для записи параметров
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0 # Итоговое кол-во баллов

    # Рассчитываем кол-во слов в тексте
    words = text.split()
    total_words = len(words)

    # Вызываем функцию расчета кол-ва предложений
    total_sentences = count_sentences(text)

    # Вызываем функцию расчета кол-ва слогов
    total_syllables = count_syllables(words)

    # Вызываем функцию расчета удобочитаемости
    score = compute_readability(total_words, total_sentences, total_syllables)

    # Вызываем функцию с показателями (кому нужно)
    indicators(total_words, total_sentences, total_syllables, score)
    
    # Вызываем функцию вывода классификации удобночитаемости
    output_result(score)


# Рассчитываем кол-во предложений в тексте
def count_sentences(text):
    ''' Эта функция получает текст и возвращает кол-во предложений в тексте,
используя для подсчета предложений знаки пунктуации .!?
'''
    count = 0
    terminals = ['.','!','?']
    for i in text:
        if i in terminals: # Ищем символы завершения предложения
            count = count +1
    return count


# Суммируем получаемые слоги в тексте по каждому слову 
def count_syllables(words):
    ''' Эта функция получает список слов и возвращает общее кол-во слогов в
тексте
'''
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count


# Расситываем кол-во слогов в тексте
def count_syllables_in_word(word):
    ''' Эта функция получает слово из текста и возвращает кол-во слогов в слове.
Является вложенной функцией count_syllables(words)
'''
    count = 0
    processed_word = word

    # Проверяем, является ли последний символ в строке знаком
    if processed_word[-1] in '.,;:!?': 
        processed_word = processed_word[0:-1]
        
    # Проверяем, является ли последний символ в строке буквой eE,
    # которые не являются слогом в конце слова
    if processed_word[-1] in 'eE': 
        processed_word = processed_word[0:-1]

    # Если кол-во символов в слове меньше или равно 3, то возвращаем значение
    if len(processed_word) <= 3:
        return 1

    # объявляем список гласных
    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False # Переменная для учета предыдущей гласной

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    # Если последний символ строки является  yY, то увеличиваем счетчик слогов
    if processed_word[-1] in 'yY':
        count = count +1
        
    return count


# Фунция расчета удобночитаемости
def compute_readability(total_words, total_sentences, total_syllables):
    ''' Эта функция получает переменные, расчитывает индекс удобочитаемости
и возвращает его
'''
    score = (206.835-1.015*(total_words/total_sentences)
             - 84.6*(total_syllables/total_words))
    return score

# Функция вывода итоговой классификации
def output_result (score):
    ''' Эта функция получает индекс удобочитаемости и выводит информацию
о уровне удобочитаемости текста
'''
    if score>= 90:
        print('Уровень 5-го классаы')
    elif score>= 80:
        print('Уровень 6-го класса')
    elif score>= 70:
        print('Уровень 7-го класса')
    elif score>= 60:
        print('Уровень 8-9-го классов')
    elif score>= 50:
        print('Уровень 10-11-го классов')
    elif score>= 30:
        print('Уолвень студента вуза')
    else:
        print('Уровень выпускника вуза')

# Вывод показателей расчетов
def indicators(total_words, total_sentences, total_syllables, score):
    ''' Эта функция получает расчитанные переменные формулы
и индекс удобочитаемости и выводит значения показателей функции
'''
    print(total_words, 'слов')
    print(total_sentences, 'предложений')
    print(total_syllables,'слогов')
    print(score,'- удобочитаемость')


# Передаем текст на оценку в начальный метод!
if __name__ == '__main__':
    import ch1text
    print('Текст 1-й главы:')
    computer_readavility(ch1text.text)



    

