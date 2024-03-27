
# Калькулятор банок краски на площадь. кол-во банок = высота * ширина / покрытие 1 банки
#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
	cans = math.ceil(height * width / cover)
	print(f"Вам потребуется: {cans} банок краски.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Высота стены: "))
test_w = int(input("Ширина стены: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


