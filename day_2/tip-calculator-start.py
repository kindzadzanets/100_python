#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
# преобразовать, полученные данные из "строка" в "дробь" и сохранить в переменную.
bill = float(input("What was the total bill? $"))

# преобразовать, полученные данные из "строка" в "число" и сохранить в переменную.
tip = int(input("What percentage tip would you like to leave: 10, 12, or 15? "))

# преобразовать, полученные данные из "строка" в "число" и сохранить в переменную.
persons = int(input("How many people are splitting the bill? "))

# вычислить коэфициэнт чаевых "1.процент от суммы" и сохранить в переменную.
tip_ratio = tip / 100 + 1

# округлить результат вычисления до 2ух знаков после запятой и сохранить в переменную.
bill_piece = round(bill / persons * tip_ratio, 2)

# отобразить сумму на человека
print(f"Each person should pay: ${bill_piece}")