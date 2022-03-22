from tkinter import *
import math

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
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        timer_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "bold"), highlightthickness=0)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50, "bold"), highlightthickness=0)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"), highlightthickness=0)
        count_down(work_sec)

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
        if reps % 2 == 0:
            tick_label.config(text="✔" ,bg=YELLOW, fg=GREEN, font="bold", highlightthickness=0)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"), highlightthickness=0)
timer_label.grid(column=2, row=0)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)


# Start Button
start_button = Button(command=start_timer, text="Start", bg="white", fg="black", highlightthickness=0, font="bold")
start_button.grid(column=1, row=2)


# Reset Button
reset_button = Button(command=reset_timer, text="Reset", bg="white", fg="black", highlightthickness=0, font="bold")
reset_button.grid(column=3, row=2)


# Tick Label
tick_label = Label(bg=YELLOW, fg=GREEN, font="bold", highlightthickness=0)
tick_label.grid(column=2, row=4)


window.mainloop()
