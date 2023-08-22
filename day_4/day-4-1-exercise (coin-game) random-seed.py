#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
print("It's a coin toss game!")

# seed = int(input("Give me a seed number!!!\n"))
# random.seed(seed)

coin_side = random.randint(0, 1)
# print(coin_side)

if coin_side == 1:
	print("Heads")
else:
	print("Tails")
