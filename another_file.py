from turtle import Turtle, Screen

eldar = Turtle()
screen = Screen()

eldar.shape('turtle')
eldar.color('orange')

def move():
    eldar.penup()
    eldar.forward(20)

def back():
    eldar.penup()
    eldar.backward(20)

def lef():
    eldar.penup()
    eldar.setheading(90)

def right():
    eldar.penup()
    eldar.setheading(270)

screen.listen()
screen.onkey(move, 'w')
screen.onkey(back, 's')
screen.onkey(lef, 'a')
screen.onkey(right, 'd')

screen.exitonclick()