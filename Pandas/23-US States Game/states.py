from turtle import Turtle
import pandas as pd


class States(Turtle):
    
    def __init__(self, data):
        super().__init__()
        self.ht()
        self.penup()
        self.data = data

    def mark_state(self, state_name):
        state_data = self.data[self.data.state == state_name]
        x, y = int(state_data.x), int(state_data.y)

        self.goto(x, y)
        self.write(state_name, align="center", font=("Arial", 8, "normal"))

