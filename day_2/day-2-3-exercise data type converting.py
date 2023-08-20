# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# вычислить остаток лет, переведённый из "строки", в "целое число" исходя из того-что весь срок жизни - 90 лет
rest_life_years = 90 - int(age)

# вычислить остаток в иных величинах
rest_life_month = rest_life_years * 12
rest_life_weeks = rest_life_years * 52
rest_life_days = rest_life_years * 365

# преобразовать все отображаемые данные в "строку" путём добавления f"" и помещая все переменные в {}
message = f"You have {rest_life_days} days, {rest_life_weeks} weeks, and {rest_life_month} months left."
# отобразить сообщение
print(message)








