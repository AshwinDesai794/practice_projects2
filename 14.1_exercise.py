from game_data_14exercise import data, logo, vs
import random

print(logo)

# print(data[1]["follower_count"])
score = 0

# Auto Choose 2 random data to compare
quest_1 = (data[random.randint(0, len(data))])
# print(quest_1)

xyz = True
while xyz:
    print("\nNext\n")

    print(f"Compare A: {quest_1['name']}, {quest_1['description']}, from {quest_1['country']} \n")
    print(quest_1['follower_count'])

    print(vs)

    quest_2 = (data[random.randint(0, len(data))])
    if quest_1 == quest_2:
        quest_2 = (data[random.randint(0, len(data))])

    # print(quest_1)
    print(f"Compare B: {quest_2['name']}, {quest_2['description']}, from {quest_2['country']} \n")
    print(quest_2['follower_count'])

    # ask user which data has more followers
    ans = input("Who has more followers Type 'A' or 'B' ? ").lower()

    # compare 2 random data and store soln in c and compare c with answer\
    def compare_data(que1, que2, p_ans):
        if que1 > que2:
            x = "a"
        else:
            x = "b"
        return x


    q_greater = compare_data(que1=quest_1['follower_count'], que2=quest_2['follower_count'], p_ans=ans)

    if ans == q_greater:
        print("you win")
        score += 1
        print(f"Your score is {score}\n")
        quest_1 = quest_2

    else:
        print(f"you lose. Your Final Score is {score}")
        break

# if answer is right score+1 else return/break
# Put above all points in a loop

# clear the screen ; Don't know how-->
