import random
import list

word_list = list.word_list
stages = list.stages
lifes = len(stages) - 1
chosen_word = random.choice(word_list).upper()

print(list.logo)
# print(chosen_word)

display = []
for symbol in chosen_word:
	display.append("_")
print(display)
print(stages[lifes])


while ("_" in display) and (lifes > 0):
	guess = input("\nПожалуйста назовите букву:\n")[0].upper()
	if guess in chosen_word and guess not in display:
		# моё иное решение:
		# position = 0
		# for char in chosen_word:
		# 	if char == guess:
		# 		display[position] = char
		# 	position += 1
		for position in range(len(chosen_word)):
			char = chosen_word[position]
			if char == guess:
				display[position] = char
	elif guess in display:
		print("\nэта буква уже открыта")
	else:
		lifes -= 1
		print("\nнет такой буквы в этом слове\n" + stages[lifes])

	print(display)

if "_" not in display:
	print("\nМОЛОДЕЦ!!! Ты спас висельника!")
else:
	print("\nПОВЕШЕН! это было слово: " + chosen_word)