#Younes Bakir
#9/15/25
#Turtle Project: MSPaint Ripoff
#Extra: Color shifting line

import turtle
import colorsys

hue = 0

def set_turtle_color():
    global hue

    #HSV to RGB converter, and if colorsys returns values in [0,1] then we multiply that value by 255
    rgb = colorsys.hsv_to_rgb(hue, 1, 1) 

    #Set pen color, the values are expected in [0,1]
    t.pencolor(rgb)

    #Increment hue 
    hue += 0.03
    if hue >= 1:
            hue = 0

t = turtle.Turtle()
s = turtle.Screen()
turtle.bgcolor('lightgray')

def up():
    set_turtle_color()
    t.forward(50)

def down():
    set_turtle_color()
    t.backward(50)

def left():
    set_turtle_color()
    t.left(45)

def right():
    set_turtle_color()
    t.right(45)

def movement():
    pass
s.listen()
s.onkey(up, 'w') #Go up if w is pressed
s.onkey(down, 's') #Go down if s is pressed
s.onkey(left, 'a') #Rotate if a is pressed
s.onkey(right, 'd') #Rotate if d is pressed

turtle.done()
