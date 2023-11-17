
from turtle import *
from random import random
import turtle




# win = turtle.Screen()
# # win.bgpic('bacground.gif')
# win.register_shape('Aprentissage_des_classes\Hit_me_ver_class\image.gif')

# target = turtle.Turtle()
# target.shape('Aprentissage_des_classes\Hit_me_ver_class\image.gif')

# \
# turtle = Turtle()

# turtle.addshape('image.gif')
# turtle.shape('image.gif')

t = Turtle()
step = 5

class poule():
    def __init__(self,color,shape,width,speed):
        t.color(color)
        t.shape(shape)
        t.width(width)
        t.penup()
        t.speed(speed)

    def draw(x, y):
        t.pendown()
        t.goto(x, y)
        

# def move(x, y):
#     t.penup()
#     t.goto(x, y)
#     pendown()


    def Up():
        t.goto(t.xcor(), t.ycor() + step)

    def down():
        t.goto(t.xcor(), t.ycor() - step)

    def droite():
        t.goto(t.xcor() + step , t.ycor())

    def gauche():
        t.goto(t.xcor() - step , t.ycor())
    scr = t.getscreen()
    t.ondrag(draw)


    scr.onkey(Up, 'Up')
    scr.onkey(down, 'Down')
    scr.onkey(gauche, 'Left')

    scr.onkey(droite, 'Right')


# scr.onscreenclick(move)

    scr.listen()




class voiture():
    def init        
exitonclick()





