
print("Welcome to the treasure island")

a = input("Where do you want to go? left or right?").lower()

while True:
    if a == "right":
        print("Game Over")
        break
    elif a == "left":
        b = input("swim or wait?").lower()
        if b == "swim":
            print("Game over")
            break

        elif b == "wait":
            c = input("Which Door red yellow blue?").lower()
            if c=="yellow":
                print("You win")
                break
            else:
                print("Game Over")


        else:
            print("invalid input")
            break

    else:
        print("invald input")
        continue
