import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
direction = [0, 90, 180, 270]
colours = ["cornflower blue", "forest green", "chartreuse", "olive drab", "dark khaki", "olive",
           "dark olive green", "khaki", "yellow", "goldenrod", "sienna", "navajo white", "orange",
           "firebrick", "red", "blue"]
#direction_choice = random.choice(direction)
# print(direction_choice)
tim.speed("fastest")

for _ in range(200):
    tim.pensize(random.randint(0, 10))
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()