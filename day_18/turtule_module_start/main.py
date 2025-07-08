from turtle import Turtle, Screen
import random

# from turtle import *  - импорт всех классов из модуля. далее можно также указывать только класс без модуль.класс, 
# но это может быть не очень удобно, так как много классов залезет в пледложку и атрибуты с функциями будут рекомендоваться непонятно откуда
# import turtle as t - алиас для модуля. дальше можно: turtle = t.turtle()

# import heroes - импорт внешнего - невстроенного модуля требует установки через pip
# print(heroes.gen()) - метод класса можно вызвать напрямую - без создания объекта


turtle = Turtle()
screen = Screen()


screen.bgcolor("tan")
screen.title("Victor and George")
turtle.shape("arrow")
turtle.color("red")


for move in range(4):  #нарисовать квадрат
    turtle.left(90)
    turtle.forward(30)

for move in range(15):  #нарисовать пунктир
    turtle.forward(10)
    turtle.up()
    turtle.forward(10)
    turtle.down()



screen.exitonclick()