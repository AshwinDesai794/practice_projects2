alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction =  input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# print(len(text))
# print(text)
# print(text[1], "\n")
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(plain_text, shift_amount):
    textList = []
    for i in plain_text:
        if alphabet.index(i)+int(shift) >25:
            tex = alphabet[alphabet.index(i) + int(shift_amount)-26]
            textList.append(tex)
        else:
            tex = alphabet[alphabet.index(i)+int(shift_amount)]
            textList.append(tex)
        #textList[i] = alphabet[index(text[i])+int(shift)]
    print(textList)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

if direction=="encrypt":
    encrypt(plain_text=text, shift_amount=shift)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(cipher_text, shift_amount):
    textList = []
    for i in cipher_text:
        if alphabet.index(i) - int(shift) < 0:
            tex = alphabet[26-alphabet.index(i) - int(shift_amount)]
            textList.append(tex)
        else:
            tex = alphabet[alphabet.index(i) - int(shift_amount)]
            textList.append(tex)
        # textList[i] = alphabet[index(text[i])+int(shift)]
    print(textList)




#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "decrypt":
    decrypt(cipher_text=text, shift_amount=shift)