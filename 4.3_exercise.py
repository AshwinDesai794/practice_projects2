import random

#name=[]
#name = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

name = input("Enter names?")

name = name.split(', ')

print(name[random.randint(0, len(name)-1)], "Is going to pay the bill")


#Joining 2 Lists:-
'''
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

all = fruits+vegetables                 #Joining 2 strings
dirty_dozen = [fruits, vegetables]      # String inside strings

print(dirty_dozen)
print(fruits)
print(all)
'''


