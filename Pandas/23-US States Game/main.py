import turtle
import pandas as pd
from states import States

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/samui/Desktop/Python/23-US States Game/blank_states_img.gif"
screen.bgpic(image)

score = 0
correct_guesses = []

data = pd.read_csv("23-US States Game/50_states.csv")
states_list = data.state.to_list()
state = States(data)


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States", prompt="What's another state's names?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("23-US States Game/States to learn.csv")
        break
    if answer_state in states_list and answer_state not in correct_guesses:
        state.mark_state(answer_state)
        correct_guesses.append(answer_state)
        score += 1







