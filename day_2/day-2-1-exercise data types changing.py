# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# отобразить тип данных в переменной
print(type(two_digit_number))

# изменить тип данных первого символа в строке на "целое число" и присвоить его новой переменной
first_digit = int(two_digit_number[0])
# изменить тип данных второго символа в строке на "целое число" и присвоить его новой переменной
second_digit = int(two_digit_number[1])
# отобразить сумму переменных
print(first_digit + second_digit)

# или так:
print(int(two_digit_number[0]) + int(two_digit_number[1]))



