import random

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100\n")

level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
num = random.randint(1, 100)

count =0

if level =="easy":
    count = count+ 10
    print("you ave chosen a difficult level : 10 life")

else:
    count = count+5
    print("you ave chosen a difficult level : 5 life")

while count> 0:
    guess = int(input("Enter your guess? "))

    # Put this in function
    
    if guess==num:
        print("you win")
        break

    elif guess> num:
        print("Too High")
        count -= 1
        print(f"You have {count} lifes left")

    elif guess< num:
        print("Too low")
        count -= 1
        print(f"You have {count} lifes left")

if count==0:
    print("\n You are out of guess; you lose")

