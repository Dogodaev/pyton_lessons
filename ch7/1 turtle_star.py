import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')
pokey = turtle.Turtle()
pokey.shape('turtle')
pokey.color('red')


def star(the_turtle):
    global num
    for i in range(5):
        the_turtle.forward(100)
        if num:
            the_turtle.right(144)
        else:
            the_turtle.left(144)
    

num = True
star(slowpoke)
num = False
pokey.left(180)
star(pokey)



turtle.mainloop()
