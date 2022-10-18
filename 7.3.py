import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
for x in range(len(chosen_word)):
    display.append("_ ")
display = "".join(display)
print(display)

end_of_game = False
final_word = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            final_word.append(letter)
        else:
            final_word.append("_")

    print("".join(final_word))

    if "_" not in final_word:
        end_of_game =True

