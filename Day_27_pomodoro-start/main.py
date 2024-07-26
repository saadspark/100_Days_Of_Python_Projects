from tkinter import *
from tkinter import PhotoImage
from timeit import default_timer as timer
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset() :
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    label_title.config(text='Timer')
    label_check.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_title.config(text='Long Break',fg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_title.config(text='Short Break',fg=RED)
    else:
        count_down(WORK_MIN*60)
        label_title.config(text='Work', fg=GREEN)
   

def end_timer():
    window.after_cancel(timer)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec == 0 :
        count_sec = "00"
    elif count_sec < 10 :
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if(count > 0) :
       global timer
       timer =   window.after(1000, count_down, count-1)
    else :
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        label_check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

button_start = Button(text='Start',command=start_timer)
button_start.grid(column=0, row=2)

button_end = Button(text='Reset',command=reset)
button_end.grid(column=3, row=2)

label_title = Label(text='Timer', font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(column=2, row=0)

label_check = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_check.grid(column=2, row=3)

window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

canvas = Canvas(width=200, height=224,bg=YELLOW)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.grid(column=2, row=1)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


window.mainloop()