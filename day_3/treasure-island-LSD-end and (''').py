print('''
WELCOME TO YOUR FIRST LSD TRIP!
 _         _ 
| |       | |
| |___  __| |
| / __|/ _` |
| \__ \ (_| |
|_|___/\__,_|

''')

drug = input("So Neo it's time to choose BLUE or RED?\n")
drug = drug.lower()
if drug == "red" or drug == "blue":
    print("Good choice! Let's go")
    mirror = input(
        "Just look at the mirror, it's looks like lake. It's so beautiful... Wanna touch it? (Y/N)\n").lower()
    if mirror == "y":
        stay = input(
            "Oh damn! Glass starts to flow on you like watter. It's better to RUN away....\nOr you want to STAY?\n").lower()
        if stay == "stay":
            safe = input(
                "It's flowing higher and higher to your neck... are you still sure that it's safely? (Y/N)\n").lower()
            if safe == "y":
                chill = input(
                    "It filled your throat and you began to choke! Somebody told you that you should CHILL out, because it's just your emagination.\nOr maybe you need HELP? What you gonna do now?\n").lower()
                if chill == "chill":
                    coffin = input("You're dead.\nWhich collor of coffin do you prefer: BROWN, BLUE, GREEN?\n")
                    print('''GAME OVER MUTHER FUCKER!




        _.---,._,'
       /' _.--.<
         /'     `'
       /' _.---._____
       \.'   ___, .-'`
           /'    \\             .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
        |                 |           |
        |                 |           |
         \               \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^	 
	 ''')

                else:
                    print("YOU WIN! It's better to stay alive...")
            else:
                print("YOU LOOSE!\nStay home stupid chicken.")
        else:
            print("YOU LOOSE!\nStay home stupid chicken.")
    else:
        print("YOU LOOSE!\nStay home stupid chicken.")

else:
    print("YOU WIN! Stay clear and all be FINE.")

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# #Write your code below this line 👇

# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")