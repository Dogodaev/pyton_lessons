import random


def generation_map():
    '''Данный метод получает параметр высоты и ширены и генерирует карту мира'''
    global grid_model, next_grid_model, height, width
    
    grid_model = [0] * height
    next_grid_model = [0] * height
    for i in range(height):
        grid_model[i] = [0] * width
        next_grid_model[i] = [0] * width


def next_gen():
    ''' Данный метод получает параметры высоты и ширены карты и вычисляет следующий цикл жизни клеток '''
    global next_grid_model, height, width
    
    for i in range(height):
        for j in range(width):
            count = count_neighbors (i, j)
            if count == 2 or count == 3:
                next_grid_model[i][j] = 1
            else:
                next_grid_model[i][j] = 0
            #print('По причине наличия', count, 'клеток рядом с основной клеткой')
            #state_life(next_grid_model[i][j], i, j)
    castling()


def state_life(num, i, j):
    '''Данный метод получает статус жизни клетки и её адрес и выводит текствовое представление её состояния'''
    if num == 1:
        print ('Клетка',i,j,'ЖИВА')
    else:
        print('Клетка',i,j,'мертва')
    

def count_neighbors (row, col):
   '''Данный мотод получает адрес клетки и размер мира. Вычисляет кол-во ЖИВЫХ соседей у клетки'''
   global grid_model, height, width
   count = 0
   
   if row-1 >= 0:
        count = count + grid_model[row-1][col]
   if (row-1 >= 0) and (col-1 >= 0):
       count = count + grid_model[row-1][col-1]
   if (row-1 >= 0) and (col+1 < width):
       count = count + grid_model[row-1][col+1]
   if col-1 >= 0:
       count = count + grid_model[row][col-1]
   if col + 1 < width:
       count = count + grid_model[row][col+1]
   if row + 1 < height:
       count = count + grid_model[row+1][col]
   if (row + 1 < height) and (col-1 >= 0):
       count = count + grid_model[row+1][col-1]
   if (row + 1 < height) and (col+1 < width):
       count = count + grid_model[row+1][col+1]
   return count

def randomize():
    '''Метод получает параметры размера мира и на их основе генерирует случайные значения статуса клеток'''
    global grid_model, height, width

    for i in range(height):
        for j in range(width):
            grid_model[i][j] = random.randint(0,1)
            #state_life(grid_model[i][j], i, j)

def castling():
    '''Метод необходим для смены карты для многоразового вычисления статуса жизни на карте'''
    global grid_model, next_grid_model
    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp

def main():
    '''основной метод, в нем задается рамер мира и выполнятся все команды '''    
    generation_map()
    randomize()
    next_gen()
    castling()



grid_model= []
next_grid_model = []
height = 100
width =100

if __name__ == '__main__':
    main()


if __name__ != '__main__':
    generation_map()
    #randomize()
    
