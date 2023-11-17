from turtle import *

v = 100
step = 5

class Character(Turtle):
    def __init__(self, color, shape, x, y, speed, width):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.penup()
        self.goto(x, y)
        self.speed(speed)
        self.width(width)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - step)

    def move_right(self):
        self.goto(self.xcor() + step, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - step, self.ycor())

class MovingSquare(Character):
    def move(self, distance):
        self.forward(distance)
        if self.xcor() >= 100 or self.xcor() <= -100:
            self.forward(-distance)

t = Character('red', 'turtle', 0, 0, v, 5)
t2 = MovingSquare('blue', 'square', -100, 200, v, 5)
t3 = MovingSquare('blue', 'square', 100, 100, v, 5)
t4 = Character('green', 'triangle', 0, 250, v, 5)

scr = t.getscreen()

# def move_up():
#     t.move_up()

# def move_down():
#     t.move_down()

# def move_right():
#     t.move_right()

# def move_left():
#     t.move_left()

scr.onkey(t.move_up, 'Up')
scr.onkey(t.move_down, 'Down')
scr.onkey(t.move_left, 'Left')
scr.onkey(t.move_right, 'Right')

scr.listen()

while t2.xcor() < 100 and t3.xcor() > -100:
    for i in range (100):
        t2.move(2)
        t3.move(-2)
    for i in range (100):
        t2.move(-2)
        t3.move(2)
    
    

exitonclick()
