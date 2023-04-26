from tkinter import *
import model
'''управлене цветом можно запилить через отдельный массив, и на каждом ходу
првоерять, перешла ли переменная в 0 или осталась 1, если осталась 1,
то менять её цвет и добавлятьк параллельному массиву +1 в зависимости
от цвета '''


def setup():
    '''В данном методе задается окно игры и имеющиеся виджеты. '''
    global root, grid_view, cell_size, start_button, clear_button, choice
    root = Tk()
    root.title('The Game of Life') #  Задаем имя окну
    grid_view = Canvas( root, width = model.width*cell_size, #Настраиваем окно игры
                        height = model.height *cell_size,
                        borderwidth = 0,
                        highlightthickness = 0,
                        bg = 'white')
    grid_view.bind('<Button-1>', grid_handler) # Привязываем клик левой кнопкой мыши кнопку к методу

    start_button = Button(root, text = 'Start', width = 12)# Создаем кнопку Start
    start_button.bind('<Button-1>', start_handler) # Привязываем клик левой кнопкой мыши кнопку к методу

    clear_button = Button(root, text = 'Clear', width = 12)# Создаем кнопку Clear
    clear_button.bind('<Button-1>', clear_handler) # Привязываем клик левой кнопкой мыши кнопку к методу
    
    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root,choice,'Choose a Pattern',# Создаем выпадающиц список
                                    'glider',
                                    'glider gun',
                                    'random',
                        command = option_handler)
    option.config(width = 20)# увеличиваем размер виджета

    # Задаем расположение кнопок и игрового поля
    grid_view.grid(row = 0, columnspan = 3, padx = 20, pady = 20)
    start_button.grid(row = 1, column = 0, padx = 20, pady = 20)
    option.grid(row = 1, column = 1, padx = 20)
    clear_button.grid(row = 1, column = 2, sticky = E, padx = 20, pady = 20)

def grid_handler(event):
    '''Функция позволяет вручную вносить клетки в игровое поле'''
    global grid_view, cell_size

    x = int(event.x / cell_size)
    y = int(event.y / cell_size)

    if model.grid_model[x][y] == 1:
        model.grid_model[x][y] = 0
        draw_cell(x,y,'white')
    else:
        model.grid_model[x][y] = 1
        draw_cell(x,y,'black')


def option_handler(event):
    '''Функция выбора варианта действия из списка Choose a Pattern'''
    global is_running, start_button, choice

    is_running = False
    start_button.configure(text = 'Start')
    
    selection = choice.get()
    if selection == 'glider':
        clear_handler(event)
        glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]
        model.load_pattern(glider_pattern,10,10)
    elif selection == 'glider gun':
        clear_handler(event)
        glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        model.load_pattern(glider_gun_pattern,10,10)
    elif selection == 'random':
        model.randomize()

    update()

def start_handler(event):
    '''Метод управляет кнопкой Start и запускает процесс расчета
        и представления жизни на карте. Так же меняет имя кнопки на Pause'''
    global is_running, start_button
    if is_running:
        is_running = False
        start_button.configure(text = 'Start')
    else:
        is_running = True
        start_button.configure(text = 'Pause')
        update()


def clear_handler(event):
    '''Метод очищает игровое поле '''
    global is_running, start_button
    for i in range(model.height):
        for j in range(model.width):
            model.grid_model[i][j] = 0

    is_running = False
    start_button.configure(text = 'Start')
    update()


def update():
    '''Метод запускает расчет следующего этапа(ов) жизни на карте и производит её
        визуализацию'''
    global grid_view, root, is_running

    grid_view.delete(ALL)
    if is_running:
        model.next_gen()

    for i in range(model.height):
        for j in range(model.width):
            if model.grid_model[i][j] ==1:
                draw_cell(i, j, 'black')
    if is_running:
        root.after(100, update)


def draw_cell(row, col, color):
    '''Косметический метод. Получает адрес клетки и цвет заливки. '''
    global grid_view, cell_size

    if color == 'black':
        outline = 'grey'
    else:
        outline = 'white'
    grid_view.create_rectangle(row * cell_size,
                               col * cell_size,
                               row * cell_size + cell_size,
                               col * cell_size + cell_size,
                               fill = color, outline = outline)
    
        

cell_size = 5
is_running = False

if __name__ == '__main__':
    setup()
    update()
    mainloop()
    
