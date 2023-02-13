import turtle
import random

def setup ():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')

    turtle_ycor = [-60 , -40, -20, 0, 20, 40, 60]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green', 'yellow', 'grey']

    for i in range(len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle. color(turtle_color[i])
        turtles.append(new_turtle)

def race():
    winner = False
    global turtles
    finishline = 540
    while not winner:
        for current_turtle in turtles:
            current_turtle.forward(random.randint(1,5))

            xcor = current_turtle.xcor()
            if xcor >= finishline:
                winner = True
                color = current_turtle.color()
                print('Победитель заезда --', color[0])

turtles = []
setup()
race()

turtle.mainloop
