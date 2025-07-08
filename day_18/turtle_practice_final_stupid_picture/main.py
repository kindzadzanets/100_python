import turtle
import random


rgb_colors_list = [
    (202, 161, 90),
    (165, 66, 52),
    (158, 58, 73),
    (128, 163, 190),
    (213, 84, 55),
    (225, 206, 119),
    (65, 37, 55),
    (202, 136, 161),
    (57, 50, 104),
    (42, 38, 66),
    (65, 82, 147),
    (195, 79, 118),
    (129, 178, 157),
    (81, 153, 114),
    (157, 170, 69),
    (76, 127, 97),
    (109, 44, 38),
    (114, 42, 52),
    (96, 104, 168),
    (161, 200, 217),
    (219, 175, 186),
    (225, 175, 168),
    (181, 186, 212),
    (174, 202, 189),
    (83, 150, 152),
    (0, 1, 0),
    (82, 60, 43),
]

# 10 х 10 точек с интервалами  в 50 
# размер точки - 20
dotti = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)
dotti.speed(0)
dotti.shape("circle")
# dotti.color(255, 255, 255) or
dotti.hideturtle()
dotti.shapesize(0.1)
dotti.pensize(2)

dotti.up()

y = -225
for _ in range(10):
    dotti.teleport(-225, y)
    y += 50
    for _ in range(10):
        dotti.dot(20, random.choice(rgb_colors_list))
        dotti.fd(50)
    # dotti.down()
# dotti.dot(20, random.choice(rgb_colors_list))

screen.exitonclick()
# dotti.position()
# (100.00,-0.00)


