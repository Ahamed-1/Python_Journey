from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
running_timer = None

# Math module in python provides mathematical functions which are useful for mathematical calculations. Math module in python contains various mathematical functions which represent complex mathematical calculations. Math module in python is used to access mathematical functions which are useful for mathematical calculations.
# Canvas Widget in tkinter in Python is used to implement the structured graphics. It is used to draw shapes, text, images, and other objects. The Canvas is a rectangular area intended for drawing pictures or other complex layouts. You can place graphics, text, widgets or frames on a Canvas.
# The Canvas widget provides structured graphics facilities for Tkinter. This is a highly versatile widget which can be used to draw graphs and plots, create graphics editors, and implement various kinds of custom widgets.

# Dynamic Typing: Python is a dynamically typed language. This means that you don't have to declare the type of a variable when you define it; Python just figures it out based on how you are setting the variable. You can always use the type() function to know the type of a variable.
# PhotoImage class is used to add images to the Tkinter window. It is used to display images in the Tkinter window. The PhotoImage class can read GIF and PGM/PPM images from files:
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(running_timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer.config(text = "Timer")
    tick.config(text = "")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        timer.config(text = 'Break', fg = RED)
        count_down(long_break_sec)


    elif reps % 2 == 0:
        timer.config(text = 'Break', fg = PINK)
        count_down(short_break_sec)

    else:
        timer.config(text = 'Work', fg = GREEN)
        count_down(work_sec)



def count_down(count):
    global start_pomodoro
    count_min = math.floor( count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")

    if count > 0:
        global running_timer
        running_timer = window.after(1000, count_down, count-1)
        # window.after is used to call a function after a certain amount of time. The first argument is the time in milliseconds. The second argument is the function that you want to call.
    else:   
        start_timer()
        marks = ''
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        tick.config(text = marks)

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg= YELLOW)


tomato_img = PhotoImage(file="./day_28/tomato.png")

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness = 0)
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer.grid(row=0, column=1)

tick = Label(bg=YELLOW, fg=GREEN, font= (FONT_NAME, 10, "bold"))
tick.grid(row=3, column=1)

start = Button(text="Start", highlightthickness = 0, font= (FONT_NAME, 10, "bold"), command = start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness = 0, font= (FONT_NAME, 10, "bold"), command= reset_timer)
reset.grid(row=2, column=2)

window.mainloop()