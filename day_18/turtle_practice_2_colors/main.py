from turtle import Turtle, Screen
import random
import turtle


colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "black",
    "white",
    "gray",
    "brown",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "navy",
    "teal",
    "lime",
    "maroon",
    "olive",
    "coral",
    "salmon",
    "chocolate",
    "plum",
    "orchid",
    "indigo",
    "violet",
    "tan",
    "turquoise",
    "beige",
    "crimson",
    "aquamarine",
    "azure",
    "lavender",
    "khaki",
    "thistle",
    "mint cream",
    "ivory",
    "snow",
    "honeydew",
    "sky blue",
    "light blue",
    "steel blue",
    "royal blue",
    "dodger blue",
    "deep sky blue",
    "powder blue",
    "light cyan",
    "cadet blue",
    "midnight blue",
    "dark green",
    "forest green",
    "lime green",
    "pale green",
    "spring green",
    "medium sea green",
    "sea green",
    "light green",
    "dark olive green",
    "yellow green",
    "sienna",
    "rosy brown",
    "sandy brown",
    "peru",
    "burlywood",
    "wheat",
    "moccasin",
    "navajo white",
    "peach puff",
    "bisque",
    "misty rose",
    "light salmon",
    "dark salmon",
    "tomato",
    "orange red",
    "firebrick",
    "dark red",
    "hot pink",
    "deep pink",
    "light pink",
    "medium violet red",
    "pale violet red",
    "medium orchid",
    "dark orchid",
    "dark violet",
    "blue violet",
    "medium purple",
    "slate blue",
    "medium slate blue",
    "dark slate blue",
    "gainsboro",
    "light gray",
    "dark gray",
    "dim gray",
    "slate gray",
    "dark slate gray",
    "light steel blue",
    "cornflower blue",
    "chartreuse",
    "dark khaki",
]


tim = Turtle()
screen = Screen()


# screen.bgcolor("aquamarine")
screen.title("Victor and George")
tim.shape("circle")
# tim.color("dark salmon")
tim.shapesize(0.5)
tim.speed(10)
tim.pensize(10)
turtle.colormode(255)


def random_color():
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r = random.randint(0, 255)
    return (r, g, b)


# action = {
#     "moving": [tim.forward, tim.backward],
#     "turning": [tim.left, tim.right]
# }

# for _ in range(1000):
#     random.choice(action["moving"])(20)
#     random.choice(action["turning"])(90)
#     tim.pencolor(random_color())

print(random_color())
# actions = [turtle.forward, turtle.backward, turtle.left, turtle.right]

# for _ in range(1000):
#     action = random.choice(actions)

#     if action in (actions[0], actions[1]):
#         value = 20
#     else:
#         value = 90

#     action(value)
#     turtle.color(random.choice(colors))


angle = [0, 90, 180, 270]

for _ in range(1000):
    tim.forward(20)
    tim.seth(random.choice(angle))
    tim.pencolor(random_color())


screen.exitonclick()
