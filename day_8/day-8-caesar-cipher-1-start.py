alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# alphabet.index("э") получить позицию элемента списка
# print(len(alphabet)) = 33
# print(alphabet[-32])


direction = input("Напиши 'encode' что бы закодировать, напиши 'decode' что бы декодировать:\n")
text = input("Ваше сообщение:\n").lower()
shift = int(input("Количество символов сдвига:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# # Функция для шифрования текста с использованием шифра Цезаря

# def encrypt(text, shift):
# 	encrypted_text = ""  # Создание переменной для хранения зашифрованного текста
# 	for char in text:  # Проход по каждому символу в исходном тексте
# 		if char in alphabet:  # Проверка, является ли символ буквой из алфавита
# 			shifted_index = alphabet.index(char) + shift  # Вычисление нового индекса для символа с учетом сдвига вправо
# 			shifted_char = alphabet[shifted_index % len(alphabet)]  # Получение нового символа из алфавита с учетом цикличности (ВАЖНО: пример: 6−(6÷33)×33 = 6−(0×33) = 6)
# 			encrypted_text += shifted_char  # Добавление зашифрованного символа к зашифрованному тексту
# 		else:
# 			encrypted_text += char  # Если символ не является буквой, добавляем его как есть
# 	print(encrypted_text)  # Вывод зашифрованного текста
#
# # Функция для дешифрования текста, обратная функции encrypt
# def decrypt(text, shift):
# 	decrypted_text = ""  # Создание переменной для хранения расшифрованного текста
# 	for char in text:  # Проход по каждому символу в зашифрованном тексте
# 		if char in alphabet:  # Проверка, является ли символ буквой из алфавита
# 			shifted_index = alphabet.index(char) - shift  # Вычисление нового индекса для символа с учетом сдвига влево
# 			shifted_char = alphabet[shifted_index % len(alphabet)]  # Получение нового символа из алфавита с учетом цикличности (ВАЖНО: пример: -6 % 33 = −6−(−6÷33)×33 = −6−(−1×33) = 27  - особенность питона - читай ниже)
# 			decrypted_text += shifted_char  # Добавление расшифрованного символа к расшифрованному тексту
# 		else:
# 			decrypted_text += char  # Если символ не является буквой, добавляем его как есть
# 	print(decrypted_text)  # Вывод расшифрованного текста
#
# # Основная часть программы, где выполняется выбор между шифрованием и дешифрованием
# if direction == "encode":  # Если выбрано шифрование
# 	encrypt(text, shift)  # Вызов функции для шифрования текста
# elif direction == "decode":  # Если выбрано дешифрование
# 	decrypt(text, shift)  # Вызов функции для дешифрования текста
# else:  # Если выбор некорректен
# 	print("Here only two options: 'encode' or 'decode'. Try again!")  # Вывод сообщения об ошибке

# ВАЖНО:
# Когда мы делаем деление нацело отрицательного числа, результат может быть округлен как в меньшую, так и в большую сторону в зависимости от того, какой стандарт деления используется.
#
# Например, согласно стандарту Python и большинства других языков программирования, результат деления нацело для отрицательных чисел округляется в меньшую сторону (в сторону отрицательной бесконечности).
#
# Поэтому результат деления -6 на 33 в большинстве языков программирования будет равен -1, а не 0.







# результат трудов:
def crypto(text, shift, direction):
	crypted_text = ""
	for char in text:
		if char in alphabet:
			if direction == "encode":
				shifted_index = alphabet.index(char) + shift
			elif direction == "decode":
				shifted_index = alphabet.index(char) - shift
			else:
				print("Here only two options: 'encode' or 'decode'. Try again!")
				return
			shifted_char = alphabet[shifted_index % len(alphabet)]
			crypted_text += shifted_char
		else:
			crypted_text += char
	print(crypted_text)

crypto(text,shift, direction)