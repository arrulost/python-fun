import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def compare(choice, number, turns):
    if choice > number:
        print("Too high.")
        return turns - 1
    elif choice < number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}!")


def set_difficulty():
    level = input("Choose a difficulty. 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    number = random.choice(range(1, 101))
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {number}")

    turns = set_difficulty()

    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = compare(guess, number, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The correct answer is {number}")
            return
        elif guess != number:
            print("Guess again.")


game()
