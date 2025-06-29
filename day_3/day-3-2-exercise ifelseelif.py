# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# рассчитал индекс массы тела(ИМТ) и сохранил в переменную
bmi = round(weight / height ** 2)
# блок условий для класификации результата индекса массы тела(ИМТ):
# если ИМТ меньше 18.5, отобразить ф-строку(перевод всех типов данных в строку):
if bmi < 18.5:
	print(f"Your BMI is {bmi} you are underweight.")
# если условие выше = False, проверить следующее условие, если оно = True, отобразить ф-строку
elif bmi < 25:
	print(f"Your BMI is {bmi} you have a normal weight .")
# если условие выше = False, проверить следующее условие, если оно = True, отобразить ф-строку
elif bmi < 30:
	print(f"Your BMI is {bmi} you are slightly overweight.")
# если условие выше = False, проверить следующее условие, если оно = True, отобразить ф-строку
elif bmi < 35:
	print(f"Your BMI is {bmi} you are obese.")
# если ни одно из условий !=(не равно) True, для всех остальных результатов отображать ф-строку
else:
	print(f"Your BMI is {bmi} you are clinically obese.")