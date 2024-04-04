def add(n1, n2):
	return n1 + n2


def subtract(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def divide(n1, n2):
	if n1 == 0 or n2 == 0:
		return 0
	else:
		return n1 / n2


def set_operator():
	while True:
		for key in operations:
			print(key)
		choice = input(f"Выберите оператор: ")
		if choice in operations:
			return choice
		else:
			print("Выбери символ из перечисленных ниже:")


operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}


def calculator():
	num1 = float(input("Укажите первое число: "))
	is_continue = True

	while is_continue:
		operator = set_operator()
		num2 = float(input("Укажите второе число: "))
		result = operations[operator](num1, num2)
		print(f"Вычисление: {num1} {operator} {num2} = {result}")

		if input(
				f"\nЕсли вы хотите продолжить действия с {result}, введите 'да',\nначать новое вычисление 'нет': ") == "да":
			num1 = result
		else:
			is_continue = False
			calculator()


calculator()
