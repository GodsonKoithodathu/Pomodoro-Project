import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# this function will reset the timer means change everything to initial start:
def reset_timer():
    global timer
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
# this function will start the timer once the start button is pressed:
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # this if statement is for the short break time counting it will call the count-down function if its True:
    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK, font=(FONT_NAME, 30, 'bold'))
    # this if statement is for the long break time counting it will call the count-down function if its True:
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED, font=(FONT_NAME, 30, 'bold'))
    # this if statement is for the work time counting it will call the count-down function if its True:
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 30, 'bold'))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# this is the function that is used to count down the time:
def count_down(count):
    # this is to show the exact min and sec for displaying
    time_min = math.floor(count / 60)  # if count 1500 then 1500/60 = 25 min
    time_sec = count % 60
    # this if statement will change the single digit to double-digit number (i.e if 9 then to 09):
    if time_sec < 10:
        time_sec = f"0{time_sec}"
    # this is used to show the timing on the screen:
    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
    if count > 0:
        global timer
        # this after() function is used to count the digit downwards after every 1 sec:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        mark = ""
        # this is to get hold of the every work session time to add a tick mark:
        work_session = math.floor(reps / 2)  # if rep = 1 then 1/2 = 0 and if rep = 1 then 1/2 = 1 and so on
        for _ in range(work_session):
            mark += "✔"
        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# initializing a window for the project:
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas can be used to display an image on the project screen and to display any text over the image:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, font=(FONT_NAME, 30, 'bold'), fill="white", text="00:00")
canvas.grid(row=1, column=1)

# this will display the "timer label" on the project screen:
timer_label = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# creating a start button for the project:
start_button = Button(text='Start', width=10, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# creating a stop button for the project:
reset_button = Button(text='Reset', width=10, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# this will display the "tick mark" on the project screen:
tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=2, column=1)
tick_label.config(pady=30)

window.mainloop()
