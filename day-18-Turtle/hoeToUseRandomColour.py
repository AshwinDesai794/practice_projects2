import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
direction = [0, 90, 180, 270]
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #tim.color(r, g, b)
    random_color = (r, g, b)
    return random_color

for _ in range(100):
    random_color()
    tim.pensize(random.randint(0, 10))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))