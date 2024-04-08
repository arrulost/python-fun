import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :)"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win :)"
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose :( "


def play_game():
    user_hands = []
    computer_hands = []
    end = True
    print(logo)

    for i in range(2):
        user_hands.append(deal_card())
        computer_hands.append(deal_card())

    while end:
        user_score = calculate_score(user_hands)
        computer_score = calculate_score(computer_hands)
        print(f"    You cards are : {user_hands}, and your score is: {user_score}")
        print(f"    Computer's first hand is: {computer_hands[0]}")
        if user_score > 21 or computer_score == 0 or user_score == 0:
            end = False
        else:
            user_should_deal = input("Type 'y' to get another card,type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_hands.append(deal_card())
            else:
                end = False

    while computer_score != 0 and computer_score < 17:
        computer_hands.append(deal_card())
        computer_score = calculate_score(computer_hands)
    print(f"    Your final hand was: {user_hands}, final score: {user_score}")
    print(f"    Computer's final hand was: {computer_hands}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack?, Type 'y' or 'n': ") == 'y':
    play_game()
