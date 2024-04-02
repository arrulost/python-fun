import os
from art import logo


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


bids = {}
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


end_game = True
while end_game:
    user_name = input("What is your name?: ")
    bid_price = int(input("What is your bid? $"))
    bids[user_name] = bid_price
    more_users = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    if more_users == "no":
        end_game = False
        find_highest_bidder(bids)
    elif more_users == "yes":
        clear_screen()
