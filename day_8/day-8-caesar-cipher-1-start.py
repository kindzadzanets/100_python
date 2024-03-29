alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# alphabet.index("э") получить позицию элемента списка
# print(len(alphabet)) = 33
print(alphabet[-32])


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
	encrypted_text = ""
	for char in text:
		if char in alphabet:
			shifted_index = int(alphabet.index(char) + shift)
			if shifted_index < len(alphabet):
				shifted_char = alphabet[shifted_index]
			else:
				shifted_char = alphabet[shifted_index % len(alphabet)]
			encrypted_text += shifted_char
		else:
			encrypted_text += char
	return encrypted_text

def decrypt(text, shift):
	decrypted_text = ""
	for char in text:
		if char in alphabet:
			shifted_index = int(alphabet.index(char) - shift)
			if shifted_index < len(alphabet):
				shifted_char = alphabet[shifted_index]
			else:
				shifted_char = alphabet[shifted_index % len(alphabet)]
			decrypted_text += shifted_char
		else:
			decrypted_text += char
	return decrypted_text

if direction == "encode":
	encrypt(text, shift)
elif direction == "decode":
	decrypt(text, shift)
else:
	print("Here only two options: 'encode' or 'decode'. Try again!")

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.