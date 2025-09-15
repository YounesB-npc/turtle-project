import turtle
import keyboard

t = turtle.Turtle()
s = turtle.Screen()
turtle.bgcolor('lightgray')

def up():
    t.forward(100)

def down():
    t.backward(100)

def left():
    t.left(100)

def right():
    t.right(100)

def movement():
    pass
s.listen()
s.onkey(up, 'w')
s.onkey(down, 's')
s.onkey(left, 'a')
s.onkey(right, 'd')

turtle.done()