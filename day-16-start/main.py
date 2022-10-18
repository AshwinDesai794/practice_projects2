# import turtle
# import another_module
# from turtle import Screen
#
# print(another_module.another_variable)
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")            #accessing methods
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()             #Creating an object of class Screen
# print(my_screen.canvheight)      #calling attribute canvheight
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",
["Pikachu","Squirtle","Charmander",])
table.add_column("Type",
["Electric","Water","Fire",])
table.align ="l"

print(table)



