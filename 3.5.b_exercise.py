#Love Calculator

name_1 = input("Enter First name : ").lower()
name_2 = input("Enter Second name : ").lower()

name = name_1+name_2
print(name, "\n")

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = t+r+u+e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l+o+v+e

score = int(str(true)+str(love))
print(score)

if (score < 10) or (score>90):
    print("You go together like coke and mentos")

elif (score >=40) and (score<=50):
    print("You are alright together")

else:
    print(f"Your score is {score}")