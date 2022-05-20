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
check = ""
timer = None


def reset_timer():
    global check
    global reps
    check = ""
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, "bold"))
    checks.config(text=check)


def start_timer():
    global reps
    reps += 1
    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN
    if reps % 2 == 1:
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, "bold"))
        count_down(work_sec)
    if reps % 8 == 0:
        timer_label.config(text="LONG BREAK", fg=RED, bg=YELLOW, font=(FONT_NAME, 55, "bold"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 55, "bold"))
        count_down(short_break_sec)


def count_down(count):
    count_min = int(math.floor(count / 60))
    count_sec = int(count % 60)
    if count_min < 10:
        count_min = f"0{int(count_min)}"
    if count_sec < 10:
        count_sec = f"0{int(count_sec)}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            global check
            check = check + "✔"
            checks.config(text=check)
        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

checks = Label(text=check, fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
