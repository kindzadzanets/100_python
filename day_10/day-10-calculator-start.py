def add(n1, n2):
	return n1 + n2


def subtract(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def divide(n1, n2):
	if n1 is None or n2 is None:
		return 0
	else:
		return n1 / n2


def set_operator():
	while True:
		for key in operations:
			print(key)
		choice = input(f"Выберите оператор:\n")
		if choice in operations:
			return choice
		else:
			print("Выбери символ из перечисленных выше:")


operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}

num1 = float(input("Укажите первое число:\n"))
num2 = float(input("Укажите второе число:\n"))
operator = set_operator()
set_function = operations[operator]
first_result = set_function(num1, num2)

print(f"Результат: {num1} {operator} {num2} = {first_result}")

proceed = "да"  # Устанавливаем начальное значение для продолжения цикла
while proceed == "да":
	operator = set_operator()
	set_function = operations[operator]
	num3 = float(input("Укажите новое число:\n"))
	result = set_function(first_result, num3)
	print(f"{first_result} {operator} {num3} = {result}")
	first_result = result

	proceed = input(f"Желаете ли выполнить ещё одно действие с {result}?\nда\нет: ").lower()

print("Спасибо, что воспользовались этим шлаком!")


