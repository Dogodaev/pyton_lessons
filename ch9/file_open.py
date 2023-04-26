try:
    filename = 'notthere.txt'
    file = open(filename,'r')
except:
    print('Возникла ошибка при открытии файла. Файл',filename, 'не найден')
else:
    print('Ура, файл удалось открыть!')
    file.close()
