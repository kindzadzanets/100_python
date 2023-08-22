# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇
# import random

# print("Welcome to the rock/scissors/paper!")

# choise = int(input("Choose: rock is 1, paper is 2, scissors is 3:\n"))
# if 0 < choise < 4:
# 	if choise == 1:
# 		print(rock)
# 	elif choise == 2:
# 		print(paper)
# 	elif choise == 3:
# 		print(scissors)

# 	answer = random.randint(1, 3)
# # print(answer)
# 	if answer == 1:
# 		print(rock)
# 	elif answer == 2:
# 		print(paper)
# 	elif answer == 3:
# 		print(scissors)

# 	if answer == choise:
# 		print("NO winner! 🤝")
# 	elif (choise == 1 and answer == 2) or (choise == 2 and answer == 3) or (choise == 3 and answer == 1):
# 		print("Looser!")
# 	else:
# 		print("You win!!!")


# else:
# 	print("Here is only three instruments!")


import random

print("Welcome to the rock/scissors/paper!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
instruments = [rock, paper, scissors]
choise = int(input("Choose: rock is 1, paper is 2, scissors is 3:\n"))
answer = random.randint(1, 3)

if 0 < choise < 4:
    print(instruments[choise - 1])
    print(instruments[answer - 1])

    if answer == choise:
        print("NO winner! 🤝")
    elif (choise == 1 and answer == 2) or (choise == 2 and answer == 3) or (choise == 3 and answer == 1):
        print("Looser!")
    else:
        print("You win!!!")

else:
    print("Here is only three instruments!")


