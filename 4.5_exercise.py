#Rock paper scissor Game Vs Computer
import random

rock = '''        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#
# print(rock)
# print(paper)

game = [rock, paper, scissors]

while True:
    ans = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors : "))
    # print(game[ans])
    comp = game[random.randint(0, 2)]

    if ans >=3 or ans<0:
        print("Invalid input number : Try again ")
        continue

    elif game[ans] == comp:
        print(game[ans])
        print(comp)
        print("Same answer : Play Again")
        continue

    else:
        print(game[ans])
        print(comp)
        if ans ==0:           #rock
            player = "rock"
            print("0 - rock")
            if comp == scissors:
                print("Win")
            elif comp == paper:
                print("loose")
        elif ans ==1:         #paper
            print("1 - paper")
            if comp == rock:
                print("Win")
            elif comp == scissors:
                print("loose")
        elif ans == 2:        #Scissor
            print("2 - scissors")
            if comp == paper:
                print("Win")
            elif comp == rock:
                print("loose.")



