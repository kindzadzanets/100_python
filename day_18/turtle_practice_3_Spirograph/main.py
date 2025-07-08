from turtle import Turtle, Screen
import turtle
import random


spiro = Turtle()
screen = Screen()

def random_color():
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r = random.randint(0, 255)
    return (r, g, b)

turtle.colormode(255)
spiro.speed(0)
spiro.shape("circle")
spiro.shapesize(0.3)
spiro.pensize(2)

def draw_spirograph(gap):
    for angle in range(0, 360, gap):
        spiro.pencolor(random_color())
        spiro.setheading(angle)
        spiro.circle(120, extent=None, steps=None)

draw_spirograph(5)
screen.exitonclick()