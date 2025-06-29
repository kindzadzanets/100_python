year = (int(input("Which year do you want to check? ")))

# Любой год, который делится на 4 без остатка, но делится без остатка на 100 (например, 1900) является високосным годом только в том случае, если он также без остатка делится на 400.

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("Leap year.")
		else:
			print("Not leap year.")
	else:
		print("Leap year.")
else:
	print("Not leap year.")
