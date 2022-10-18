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

def calculator():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    # print(add(8, 5))

    num1 = float(input("Whats the first number?: "))

    x= True

    while x:
        for key in operations:
            print(key)
        operation_symbol = input("Enter an operation from the line above: ")
        num2 = float(input("Whats the next number?: "))

        # answer = operations[operation_symbol](num1, num2)                   #direct
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        cont = input("Enter if do yoy want to go more press 'y' and 'a' for new calculation or 'n' to exit")
        if cont=="y":
            num1=answer
        elif cont=="a":
            calculator()
        else:
            x = False

calculator()