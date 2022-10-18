import random
import turtle as t
import random

tim = t.Turtle()
colours = ["cornflower blue", "forest green", "chartreuse", "olive drab", "dark khaki", "olive",
           "dark olive green", "khaki", "yellow", "goldenrod", "sienna", "navajo white", "orange"
           "firebrick", "red", "blue"]

def draw_shape(num_sides, colours):
    """Draws polygons on a fixed side: """
    angle = 360/ num_sides
    #tim.fillcolor(random.choice(colours))
    #tim.begin_fill()
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)

    #tim.end_fill()

#print(random.choice(colours))

for i in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(i, colours=colours)