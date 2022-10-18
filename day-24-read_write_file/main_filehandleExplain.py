# f_hand = open("my_file.txt")
# contents = f_hand.read()
# print(contents)
# f_hand.close()

# OR

# with open("my_file.txt") as f_hand:    # no need to close the file
#     contents = f_hand.read()
#     print(contents)


with open("my_file_ashwin.txt", mode="w") as f_hand:    # no need to close the file
    f_hand.write("I am Ashwin\nI am a mechanical Engineering")
    # contents = f_hand.read()
    # print(contents)
