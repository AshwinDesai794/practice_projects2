import random
from art_blackJack import logo
#print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
p_card=[]
p_card[0]=cards[random.randint(0, 12)]
p_card[1]=cards[random.randint(0, 12)]
p_card_sum= sum(p_card[0]+p_card[1])
print(f"The sum of player card is {p_card}")

comp_card=[]
comp_card[0]=cards[random.randint(0, 12)]
comp_card[1]=cards[random.randint(0, 12)]
comp_card = comp_card[1] + comp_card[2]
print(f"The Computer card is {comp_card}")
print(f"The sum of player card is {p_card}")

if comp_card or p_card ==21:
    if comp_card==21:
        hit=False
        print("You lose")
    elif p_card==21:
        hit=False
        print("you win Winner")
elif comp_card or p_card >21:
    if p_card>21:
        for i in range(0, len(p_card)):
            if p_card[i] ==11:
                p_card[i] =1

    if comp_card > 21:
        for i in range(0, len(p_card)):
            if p_card[i] == 11:
                p_card[i] = 1




hit= True
while hit:
    x = input("Enter y for Hit more cards")
    if x== "y":
        p_card+=cards[random.randint(0, 12)]
        print(p_card)
        hit =True

    else:
        hit=False

