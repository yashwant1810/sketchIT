import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.pensize(2)
turtle.colormode(255)
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.seth(tim.heading()+10)


def turn_right():
    tim.seth(tim.heading()-10)


def hide_turtle():
    tim.hideturtle()


def show_turtle():
    tim.showturtle()


def random_colour():
    choicer = random.randint(0, 200)
    choiceg = random.randint(0, 200)
    choiceb = random.randint(0, 200)
    colour_tuple = (choicer, choiceg, choiceb)
    tim.pencolor(colour_tuple)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.pencolor("black")
    tim.seth(0)
    tim.setx(0)
    tim.sety(0)
    tim.pendown()


screen.listen()
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=hide_turtle, key="1")
screen.onkey(fun=show_turtle, key="2")
screen.onkey(fun=random_colour, key="z")
screen.onkey(fun=clear_screen, key="x")
screen.exitonclick()
