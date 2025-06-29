# import turtle - импорт всего модуля
from turtle import Turtle, Screen #импорт конкретных классов из модуля

timmy = Turtle() # создание объекта из класса 
timmy.color("cornsilk", "DarkSeaGreen") # вызов метода объекта с указанием атрибутов(функции)
timmy.shape("turtle") # смена формы, например
timmy.forward(100) # двигаться вперед на 100 пикс
print(timmy) # в выводе можно видеть, что под объект выделена область на диске: <turtle.Turtle object at 0x102983380>

my_screen = Screen() 
my_screen.canvheight #обращение к конкретному атрибуту созданного объкта
print(my_screen.canvheight)


my_screen.exitonclick() #вызов метода(функции) созданного объекта