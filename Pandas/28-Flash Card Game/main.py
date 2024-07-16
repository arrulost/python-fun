from tkinter import *
import pandas as pd
from random import choice,randint
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("TKinter/28-Flash Card Game/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("TKinter/28-Flash Card Game/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- NEW WORD ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image= french_flashcard)
    flip_timer = window.after(3000, flip_card)

# ---------------------------- FLASH CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=english_flashcard)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

# ---------------------------- LEARNED WORDS ------------------------------- #

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("TKinter/28-Flash Card Game/data/words_to_learn.csv", index=False)
    
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
french_flashcard = PhotoImage(file="TKinter/28-Flash Card Game/images/card_front.png")
english_flashcard = PhotoImage(file="TKinter/28-Flash Card Game/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=french_flashcard)
canvas.grid(column=0,row=0, columnspan=2)
title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))


right = PhotoImage(file="TKinter/28-Flash Card Game/images/right.png")
right_button = Button(image=right,highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)

wrong = PhotoImage(file="TKinter/28-Flash Card Game/images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0,command=next_card)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()