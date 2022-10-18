import turtle as t
import random
from main import colour_data

tom = t.Turtle()
screen = t.Screen()
t.colormode(255)

# tom.setheading(225)
# tom.forward(250)
# tom.setheading(0)

tom.speed("fastest")
tom.hideturtle()


y = -250
for row in range(10):
    tom.penup()
    tom.goto(-300, y)
    y += 50
    for col in range(10):
        # tom.penup()
        tom.forward(50)
        tom.dot(20, random.choice(colour_data))
        # tom.stamp()
        #tom.penup()


screen.exitonclick()
