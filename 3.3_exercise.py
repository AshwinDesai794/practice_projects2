# Leap year Programme

while True:
    year = int(input("Which year do you want to check : "))

    if year % 4 == 0:
        if year % 400 == 0:               #except
            print("leap year")
        elif year % 100 == 0:             #Unless
            print("Not a leap year")
        else:
            print("leap year")

    else:
        print("Not a leap year")