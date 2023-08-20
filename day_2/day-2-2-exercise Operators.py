# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# сохранённые в переменных значения - строки, но по-факту являются десятичными дробями (float)
# для вычисления Body Mass Index необходимо вес тела в кг разделить(второе действие) на рост в м во второй степени (первое действие).
bmi = float(weight) / float(height) ** 2
print(bmi)









