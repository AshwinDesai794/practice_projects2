#use Python to get an input string
loop = True
while loop:
    pasw = input("Please enter the given password: ")

    #print paswort
    print('The password you typed was: ' + pasw)

    #check paswort
    if pasw == "TechLabs_Aachen_ST2022":
        print('Perfect! You got it!')
        print('Starting to decrypt file...')
        f = open("Key_01.txt", "r")
        key = f.read()
        temp = 5 % len(key)
        print(len(key))
        print(temp)
        print()

        keyOne = key[temp : ] + key[ : temp]
        print('Congrats! The first key is \n>> ' + keyOne + " <<")
        loop = False

    else:
        print('Password is wrong! Please retry!')