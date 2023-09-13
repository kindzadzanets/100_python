# FUNCTIONS

# содать новую функцию и задать ей имя:
def new_function():
	# внести в функцию инструкции (любые)
	print("MERHABA!")
	print("haba-haba!")

# вызвать функцию
new_function()

# цикл while: повторение цикла продолжается до тех пор пока его условие == True.
# задал переменную
number = 10
# создал цикл с условием: пока переменная больше нуля - выполнять задачи внутри цикла
while number > 0:
	# засунул нсвою функцию в цикл
	new_function()
	# с каждым кругом переменная уменьшается на 1, когда уменьшится до 0, цикл завершится
	number -=1
	# видеть сколько осталось от переменной
	print(number)

chislo = 10
while chislo > -10:
	chislo -= 1
	# так же можно в while запихнуть и ветвление:
	if chislo % 2 == 0:
		print("ЧЁТ")
	else:
		print("НЕЧЕТ")

# тренеровка тут: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json