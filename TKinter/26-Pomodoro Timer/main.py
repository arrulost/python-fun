from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F5DAD2"
RED = "#FF0000"
GREEN = "#75A47F"
DEEP_PINK = "#FF6464"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps 
    reps = 0
    title.config(text="Timer", fg=GREEN,bg=PINK,font=(FONT_NAME, 35 , "bold"))
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title.config(text="Break",fg=RED,bg=PINK,font=(FONT_NAME, 35 , "bold"))
    elif reps % 2 == 0:
        count_down(short_sec)
        title.config(text="Break",fg=DEEP_PINK,bg=PINK,font=(FONT_NAME, 35 , "bold"))
    else:
        count_down(work_sec)
        title.config(text="Work",fg=GREEN,bg=PINK,font=(FONT_NAME, 35 , "bold"))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "🗸"
        checkmark.config(text=mark)

    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=PINK)

title = Label(text="Timer", fg=GREEN,bg=PINK,font=(FONT_NAME, 35 , "bold"))
title.grid(column=1,row=0)


canvas =Canvas(width=200,height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="TKinter/26-Pomodoro Timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start",font=(FONT_NAME), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",font=(FONT_NAME), command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN,bg=PINK,font=(FONT_NAME, 35 , "bold") )
checkmark.grid(column=1, row=3)






window.mainloop()


