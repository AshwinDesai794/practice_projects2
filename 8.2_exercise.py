#Prime Number Checker :

# Write your code below this line 👇
def prime_checker(number):
    x = 0
    for i in range(2, number):

        if number%i==0:
            x+=1
    if x>0:
        print("Not a prime")
    else:
        print("Its a prime Number")

while True:
    # Write your code above this line 👆

    # Do NOT change any of the code below👇
    n = int(input("Check this number: "))
    prime_checker(number=n)


