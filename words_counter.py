text = input("enter a text:\n")
text_list = text.split(" ")
# print(text_list)

for isense in range(len(text_list)):
	text_list[isense] = text_list[isense].lower()
# print(text_list)

samoe_chastoe_slovo = ""
max_chastota = 0

for word in text_list:
	chastota = 0

	for other_word in text_list:
		if word == other_word:
			chastota += 1

	if chastota > max_chastota:
		samoe_chastoe_slovo = word
		max_chastota = chastota

print(f"\nСамое частоупотребляемое слово в тексте: '{samoe_chastoe_slovo}', оно употреблено {max_chastota} раз(а)")







# # Получаем ввод пользователя
# text = input("Введите текст: ")
#
# # Разбиваем текст на слова
# words = text.split()
#
# # Приводим слова к нижнему регистру, чтобы учитывать регистронезависимую частоту
# for i in range(len(words)):
#     words[i] = words[i].lower()
#
# # Инициализируем переменные для отслеживания самого часто повторяющегося слова
# most_common_word = None
# max_count = 0
#
# # Проходимся по каждому слову и сравниваем его с остальными словами
# for word in words:
#     count = 0
#
#     for other_word in words:
#         if word == other_word:
#             count += 1
#
#     # Если текущее слово встречается чаще, чем предыдущее "самое частое" слово
#     if count > max_count:
#         most_common_word = word
#         max_count = count
#
# # Выводим результат
# print(f"Самое часто повторяющееся слово: '{most_common_word}' (встречается {max_count} раз)")