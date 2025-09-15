#Younes Bakir
#9/15/25
#MSPaint Ripoff
#Extra: Color shifting line

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
s.onkey(up, 'w') #Go up if w is pressed
s.onkey(down, 's') #Go down if s is pressed
s.onkey(left, 'a') #Go left if a is pressed
s.onkey(right, 'd') #Go right if d is pressed

turtle.done()
