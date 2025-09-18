#Younes Bakir
#9/15/25
#Turtle Project: MSPaint Ripoff
#Extra: Color shifting line

#import required modules
import turtle
import colorsys

hue = 0

#This function will set up our color shift
def set_turtle_color():
    global hue

    #HSV to RGB converter
    rgb = colorsys.hsv_to_rgb(hue, 1, 1) 

    #Set pen color, the values are expected in [0,1]
    t.pencolor(rgb)

    #Increment hue 
    hue += 0.01
    if hue >= 1:
            hue = 0

#Set up the turtle, canvas, and adjust background color
t = turtle.Turtle()
s = turtle.Screen()
turtle.bgcolor('black')

#All these functions set up movement directions and enable the color shift
def up():
    set_turtle_color()
    t.forward(50)

def down():
    set_turtle_color()
    t.backward(50)

def left():
    t.left(45)

def right():
    t.right(45)

#These functions allow the pensize to be adjusted
def penIncrease():
    current_size = t.pensize()
    new_size = t.pensize(current_size + 1)
    t.pensize(new_size)

def penDecrease():
    current_size = t.pensize()
    new_size = t.pensize(current_size - 1)
    t.pensize(new_size)

#Controls pensize adjustments
def pensize():
    pass
s.listen()
s.onkey(penIncrease, '1') #Increase pen size if 1 is pressed
s.onkey(penDecrease, '2') #Increase pen size if 2 is pressed

#Controls movement 
def movement():
    pass
s.listen()
s.onkey(up, 'w') #Go up if w is pressed
s.onkey(down, 's') #Go down if s is pressed
s.onkey(left, 'a') #Rotate if a is pressed
s.onkey(right, 'd') #Rotate if d is pressed

turtle.done()
