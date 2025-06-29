print("This is the LOVE CALCULATOR!!!")

w_name = input("What's the girl's name?\n")
m_name = input("What's the guy's name?\n")
# .lower() - перевести строку в нижний регистр
both_names = (w_name + m_name).lower()


# .count("") - подсчитать количество конкретных символов в строке
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
true = t + r + u + e

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
# print(love_score)

if love_score < 10 or love_score > 90:
	print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
	print(f"Your score is {love_score}, you are alright together.")
else:
	print(f"Your score is {love_score}.")