import art

import os
import subprocess

#
# def clear():
#     if os.name in ('nt','dos'):
#         subprocess.call("cls")
#     elif os.name in ('linux','osx','posix'):
#         subprocess.call("clear")
#     # else:
#     #     print("\n") * 120



print(art.logo)
bid_price={}
def add_new_bid(bidder_name, bid_guess):
  #new_country = {"country": country_name, "visits": visits_time, "cities": cities_list}    or
  bid_price[bidder_name] = bid_guess

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner = bidder
        else:
            highest_bid=highest_bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")


x=True

while x:
    name = input("Enter your name?")
    bid = int(input("Enter a bid price?"))

    add_new_bid(bidder_name=name, bid_guess=bid)

    ans = input("More people to bid y/n ?")

    if ans=="y":
        #clear()
        continue
    else:
        x=False


print(bid_price)
find_highest_bidder(bid_price)









