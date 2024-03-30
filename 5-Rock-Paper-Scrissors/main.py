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
---'   ____)____
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

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
result1 = [rock, paper, scissors]
print(result1[user_input])
print("Computer choce:")

import random

num_choice = len(result1)
computer_choice = random.randint(0, num_choice - 1)

if user_input == 0 and computer_choice == 0:
    print(f"{result1[0]} \nDraw.")
elif user_input == 1 and computer_choice == 1:
    print(f"{result1[1]} \nDraw.")
elif user_input == 2 and computer_choice == 2:
    print(f"{result1[2]} \nDraw.")
elif user_input == 0 and computer_choice == 2:
    print(f"{result1[2]} \nYou won.")
elif user_input == 1 and computer_choice == 0:
    print(f"{result1[0]} \nYou won.")
elif user_input == 2 and computer_choice == 1:
    print(f"{result1[1]} \nYou won.")
elif user_input == 0 and computer_choice == 1:
    print(f"{result1[1]} \nYou lost.")
elif user_input == 1 and computer_choice == 2:
    print(f"{result1[2]} \nYou lost.")
elif user_input == 2 and computer_choice == 0:
    print(f"{result1[0]} \nYou lost.")
else:
    print("lost")






