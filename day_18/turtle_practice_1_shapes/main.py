from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()


screen.bgcolor("tan")
screen.title("Victor and George")
turtle.shape("arrow")
turtle.color("red")


# мой вариант изображения нескольких фигур, каждая последующая из которых имеет на 1 угол больше предыдущей:


# repeats = 3
# angles_amount = 3
# while angles_amount != 10:
#     for _ in range(repeats):
#         turtle.forward(30)
#         turtle.left(360 / angles_amount)
#     repeats += 1
#     angles_amount += 1
# получилось ПРОЦЕДУРНО!


colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "black",
    "white", "gray", "brown", "cyan", "magenta", "gold", "silver", "navy",
    "lime", "turquoise", "violet", "indigo", "salmon", "chocolate",
    "coral", "maroon", "aquamarine", "beige", "olive", "teal", "tan", "orchid"
]


# вариант с использованием функций:
def draw_figures(sides_amount): # функция принимает количество сторон в аргумент
    angle = 360 / sides_amount # градус угла = 360(полный круг) разделить на количество сторон
    for _ in range(sides_amount): # цикл повторится равное количеству сторон раз
        turtle.forward(60) # двидение вперед на (пикселей)
        turtle.left(angle) # поворот на количество градусов равное переменной angle

for sides_num in range(3, 11): # присваивать переменной sides_num значение количества сторон от 3 до 11(не включительно), 
    turtle.color(random.choice(colors)) # менять цвет линии, выбирая случайное его название из списка colors
    draw_figures(sides_num) # подставлять эту переменную(каждый круг цикла с новым значением) в аргумент функции.

screen.exitonclick()