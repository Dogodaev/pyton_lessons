def make_crazy_lib(filename):
    ''' Этот метод принимаем имя файла и возвращает исправленный файл'''
    try:
        file = open(filename,encoding="utf8") # Открываем файл,
        text = '' # Строка, для записи исправленного текста
        for line in file: # Цикл, по вызову метода проверки строки  и добавления
            # информации в новый текст
            text =text + process_line(line)
        file.close()
        return text
    except FileNotFoundError:
        print('Не удалось найти файл', filename + '.')
    except IsADirectoryError:
        print('Вообще-то,', filename,'- это каталог.')
    except:
        print('Не удалось прочитать файл', filename + '.')

def process_line(line):
    '''метод принимает редактируемую строку, производит поиск ключевых слов,
заменяет их и возвращает исправленную строку'''
    placeholders = ['СУЩЕСТВИТЕЛЬНОЕ', 'ПРИЛАГАТЕЛЬНОЕ', 'ГЛАГОЛ']
    processed_line = ''
    words = line.split()
    for word in words:

        if word[-1]in '!?,.:;':
            flag = True
            num = word[-1]
            
        word = word.strip('!?,.:;')
        
        if word in placeholders:
            answer = input('Введите ' + word + ':')
            processed_line = processed_line + answer + ' '
        else:
            processed_line = processed_line + word + ' '
            
        if flag:
            processed_line = processed_line[0:-1]
            processed_line = processed_line + num + ' '
            flag = False
            
    return processed_line + '\n'

def save_crazy_lib (filename, text):
    ''' Данный метод записывает полученный текст в файл с припиской crazy_'''
    file = open(filename, 'w')
    file.write(text)
    file.close()
    

def main():
    '''Основной метод. Из него производятся функций.'''
    filename = 'lib.txt'
    lib = make_crazy_lib(filename)
    print(lib)
    if lib != None:
        save_crazy_lib('crazy_' + filename,lib)


if __name__ == '__main__':
    main()


