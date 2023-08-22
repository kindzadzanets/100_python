# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# moduler(%) - разложение числа на заданное значение + остаток (максимальное количество 2 в числе + остаток - 0 или 1)
remain = number % 2
# если остаток равен 1, число - нечетное
if remain == 1:
	print("This is an odd number.")
# в остальных случаях(остаток 0) - чётное
else:
	print("This is an even number.")