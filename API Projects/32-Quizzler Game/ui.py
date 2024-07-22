from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizz_brain: QuizBrain):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280, text="question",font=("Ariel,20,italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        right = PhotoImage(file="API Projects/32-Quizzler Game/images/true.png")
        self.right = Button(image=right, highlightthickness=0, command=self.true_pressed)
        self.right.grid(column=0, row=2)
        

        wrong = PhotoImage(file="API Projects/32-Quizzler Game/images/false.png")
        self.wrong = Button(image=wrong,highlightthickness=0, command=self.false_pressed)
        self.wrong.grid(column=1,row=2)
        
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
            
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)