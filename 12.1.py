#################### Scope ############################
'''
enemies = 1        #Global variable

def increase_enemies():
    enemies = 2          #local variable
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies inside function: {enemies}")
'''


enemies = 1        #Global variable

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies+1

enemies = increase_enemies()
print(f"enemies inside function: {enemies}")