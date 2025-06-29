# # # Instructions
# # The program will ask:
# # How many letters would you like in your password?
# # How many symbols would you like?
# # How many numbers would you like?
# # The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

# # # Easy Version (Step 1)
# # Generate the password in sequence. If the user wants
# # * 4 letters
# # * 2 symbols and
# # * 3 numbers
# # then the password might look like this:
# # fgdx$*924
# # You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.


# # # Hard Version (Step 2)
# # When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
# # x$d24g*f9
# # And every time you generate a password, the positions of the symbols, numbers, and letters are different.


# #Password Generator Project:

# # добавить модуль random в код
# import random

# # создать списки изпользуемых символов
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# # запросить значения для переменных количества символов в пароле
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # # создать пустую переменную для группы символов с типом str
# # gr_letters = ""
# # # задать цикл повторений от "0"(потому-что нужен промежуток на 1 больше, чем граничное число) {заданное значение nr_letters}
# # for repeat in range(0, nr_letters):
# # 	# повторять присвоение переменной random_letter случайный знак из списка букв столько раз - сколько указанно в range.
# # 	random_letter = letters[random.randint(0, len(letters) - 1)]
# # 	# прибавлять каждое новое значение random_letters к предыдущему значению gr_letters(почему-то не решается при помощи "=+"), изменяя gr_letters на 1 новый знак - все буквы пароля в одной переменной
# # 	gr_letters = random_letter + gr_letters
# #
# # # по аналогии с буквами
# # gr_symbols = ""
# # for symbol in range(0, nr_symbols):
# # 	random_symbol = symbols[random.randint(0, len(symbols) - 1)]
# # 	gr_symbols = random_symbol + gr_symbols
# #
# # # по аналогии с буквами
# # gr_numbers = ""
# # for number in range(0, nr_numbers):
# # 	random_number = numbers[random.randint(0, len(numbers) - 1)]
# # 	# значение типа int обязательно преоразовать в строку для канкатинации
# # 	gr_numbers = str(random_number) + gr_numbers
# #
# # # собрать все знаки пароля в одной переменной
# # password_simple = gr_letters + gr_symbols + gr_numbers
# # # отобразить результат простого варианта выполнения задания
# # print(password_simple)
# #
# # # преобразовать значение переменной в список, каждый знак - отдельный элемент списка (без наличия разделителя)
# # password_list = list(password_simple)
# # # перемешать значения в списке случайным образом
# # random.shuffle(password_list)
# #
# # # задать пустую переменную для пароля с типом str
# # password_hard = ""
# # # задать цикл на сложение всех элементов списка в одну строку. (цикл повторяется столько раз, сколько в нём элементов)
# # for element in password_list:
# # 	password_hard = element + password_hard
# # # отобразить сложную версию пароля
# # print(password_hard)


# # Более изящное решение:
# # password = ""

# # for sign in range(0, nr_letters):
# # password += random.choice(letters)

# # for sign in range (0, nr_symbols):
# # password += random.choice(symbols)

# # for sign in range(0, nr_numbers):
# # password += random.choice(numbers)
# # print(password)


# # идеaльное решение:

# password_list = []
# for znak in range(0, nr_letters):
# 	password_list.append(random.choice(letters))

# for znak in range(0, nr_symbols):
# 	password_list.append(random.choice(symbols))

# for znak in range(0, nr_numbers):
# 	password_list.append(random.choice(numbers))

# random.shuffle(password_list)
# password = "".join(password_list)
# print(password)





# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# letters_part = ""
# for n in range(0, nr_letters):
# 	letters_part += random.choice(letters)


# symbols_part = ""
# for n in range(0, nr_symbols):
# 	symbols_part += random.choice(symbols)


# numbers_part = ""
# for n in range(0, nr_numbers):
# 	numbers_part += random.choice(numbers)


# password_simple = letters_part + symbols_part + numbers_part

# print(password_simple)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# хорошее решение с функцией random.sample - перемешивает символы в строке

# password_hard = "".join(random.sample(password_simple, len(password_simple)))
# print(password_hard)


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


pass_list = []
for car in range(0, nr_letters):
	pass_list.append(random.choice(letters))

for car in range(0, nr_symbols):
	pass_list.append(random.choice(symbols))

for car in range(0, nr_numbers):
	pass_list.append(random.choice(numbers))

random.shuffle(pass_list)
password = "".join(pass_list)

print(password)
