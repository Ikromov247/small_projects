from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.8
CHECK_MARK = "✔"
session_number = 1
counting = False
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_all():
    global session_number, counting, timer
    counting = False
    window.after_cancel(timer)
    session_number = 1
    canvas.itemconfig(timer_text, text="00:00")
    check_mark["text"] = ""
    status_label["text"] = " "
    canvas.itemconfig(timer_text, text="start")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_work():
    global session_number
    if not counting:
        if session_number % 8 == 0:
            countdown(LONG_BREAK_MIN*60)
            status_label["text"] = "long break"
        elif session_number % 2 == 0:
            countdown(SHORT_BREAK_MIN*60)
            status_label["text"] = "short break"
        else:
            countdown(WORK_MIN * 60)
            status_label["text"] = "working"
        check_mark["text"] = CHECK_MARK * (session_number//2)
        session_number += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global counting, timer
    counting = True
    count = int(count)
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    elif count == 0:
        counting = False
        window.focus_set()
        start_work()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=75, pady=50)
window.config(bg=YELLOW)

# canvas and picture
canvas = Canvas(width=200, height=270)
canvas.config(bg=YELLOW)
canvas.config(highlightthickness=0)
tomato_picture = PhotoImage(file="tomato.png")
canvas.create_image(100, 150, image=tomato_picture)
timer_text = canvas.create_text(100, 160, text="start", fill="white", font=(FONT_NAME, 35, "bold"))
title_text = canvas.create_text(100, 15, text="TIMER", fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=0, column=1)

# buttons
start_button = Button(window, text="Start", command=start_work, highlightthickness=0, font=(FONT_NAME, 9, "normal"))
reset_button = Button(window, text="Reset", command=reset_all, highlightthickness=0, font=(FONT_NAME, 9, "normal"))

# check marks
check_mark = Label(window, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 9, "normal"))
status_label = Label(window, text=" ", fg="black", bg=YELLOW, font=(FONT_NAME, 10, "normal"))

# place buttons and check mark under tomato image
start_button.grid(row=1, column=0, sticky=W, padx=0)
check_mark.grid(row=2, column=1, sticky=N, padx=0)
reset_button.grid(row=1, column=2, sticky=W, padx=0)
status_label.grid(row=3, column=1)

window.mainloop()
