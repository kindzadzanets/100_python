print("Welcome to the 'Python Pizza'!")
# Получить значения всех параметров заказа и сохранить их в переменные.
pizza_size = input("Which size do you prefer: S, M, L ? ").upper()
print(pizza_size)
pepperoni_add = input("Would you like to add pepperoni? (Y/N) ").upper()
extra_cheese = input("Would you like to add extra cheese? (Y/N) ").upper()

# задать переменную для цены (первоначальное значение - 0)
price = 0
# изменить значение price, в зависимости от значения переменной pizza_size ("price +=" - увеличить НА)
if pizza_size == "S": # condition
	price += 15
elif pizza_size == "M":
	price += 20
else:
	price += 25
# изменить значение уже заданного price в зависимости от pepperoni_add
if pepperoni_add == "Y": # equal condition
	if pizza_size == "S": # nested condition
		price += 2
	else:
		price += 3
# изменить значение price с учётом pepperoni_add, в зависимости от значения extra_cheese
if extra_cheese == "Y": # equal condition
	price += 1

#отобразить результат
print(f"Your final bill is: {price}$.")