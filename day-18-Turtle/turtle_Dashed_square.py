# import heroes
# print(heroes.gen())

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for x in range(4):
    for item in range(10):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)

    timmy.left(90)


screen = Screen()
screen.exitonclick()