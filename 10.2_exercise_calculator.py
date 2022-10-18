import art_calculator
from art_calculator import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return  n1*n2

def divide(n1, n2):
    return n1/n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# print(add(8, 5))

num1 = int(input("Whats the first number?: "))
num2 = int(input("Whats the second number?: "))

for key in operations:
    print(key)
operation_symbol = input("Enter an operation from the line above: ")
# answer = operations[operation_symbol](num1, num2)                   #direct
operation_function = operations[operation_symbol]
answer = operation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("Whats the next number"))
operation_function = operations[operation_symbol]
second_answer = operation_function(answer, num3)


print(f"{answer} {operation_symbol} {num3} = {second_answer}")

