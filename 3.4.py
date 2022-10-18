# Pizza Shop

bill = 0

while True:
    size = (input("\nEnter  Size of Pizza, S, M, L, ? ")).upper()

    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    else:
        print("invalid Input")
        continue
#    print(f"Your bill is : {bill}")

    add_pepperoni = input("Do you want extra pepperoni Y/N ? ").upper()
    extra_cheese = input("Do you want extra cheese Y/N ? ").upper()
    if add_pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1

    print(f"\n Final bill is {bill} \n")

    ask = input("Do you want anything else").upper()
    if ask == "Y":
        continue
    else:
        print("Thank You visit again")
        break
