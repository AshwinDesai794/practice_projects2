import turtle as t
import random

tom = t.Turtle()
t.colormode(255)
tom.speed("fastest")
degree = 0


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #tim.color(r, g, b)
    color = (r, g, b)
    return color

####################### Initial Self ###################
# def make_spiral():
#     global degree
#     tom.circle(100)
#     tom.setheading(degree)
#     degree += 10
#
# for _ in range(100):
#     tom.color(random_color())
#     make_spiral()

############## Method 2 #############

# def draw_spirograph(size_of_gap):
#     for _ in range (int(360/ size_of_gap)):
#         tom.color(random_color())
#         tom.circle(100)
#         tom.setheading(tom.heading() + size_of_gap)
#
# draw_spirograph(5)
# screen = t.Screen()
# screen.exitonclick()

###################   To Specify No of Circles #######################

def draw_spirograph(no_of_circles):
    degree = int(360/ no_of_circles)
    for _ in range(no_of_circles):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + degree)

draw_spirograph(25)
screen = t.Screen()
screen.exitonclick()

