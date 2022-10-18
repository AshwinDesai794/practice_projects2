import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for x in range(nr_letters):
    password.append(letters[random.randint(0, len(letters)-1)])
#print(password)

for y in range(nr_symbols):
    password.append(symbols[random.randint(0, len(symbols)-1)])

for z in range(nr_numbers):
    password.append(numbers[random.randint(0, len(numbers)-1)])
print(password)
print("".join(password))
random.shuffle(password)        #Shuffling the list
print(password)
print("".join(password))


#Does not work since Random nos are not unique
'''
comp_password = []
for x1 in range(len(password)):
    comp_pass = password[random.randint(0, len(password)-1)]
    comp_password.append(comp_pass)

print(''.join(comp_password))
'''