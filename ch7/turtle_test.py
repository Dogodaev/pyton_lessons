import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')
pokey = turtle.Turtle()
pokey.shape('turtle')
pokey.color('red')




print(pokey.color)
def make_square(the_turtle):
    for i in range(4):
        the_turtle.forward(200)
        the_turtle.right(90)

def make_spirel(the_turtle):
    for i in range(18):
        make_square(the_turtle)
        the_turtle.right(20)
    

make_spirel(slowpoke)
pokey.right(10)
make_spirel(pokey)


turtle.mainloop()
