import time
import tkinter
from tkinter import ttk
import math

colors = [
    'white', 'yellow', 'blue'
]
index = 0

#12%5=2 22%3=1
def update_clock():
    global index
    print(index)
    if index == 2:
        index = 0
    index += 1
    current_time = time.localtime()
    hour_angle = (current_time.tm_hour % 12 + current_time.tm_min / 60) * 30
    minute_angle = current_time.tm_min * 6
    second_angle = current_time.tm_sec * 6
    canvas.coords(hour_hand, 150, 150, 150 + 60 * math.cos((90 - hour_angle) * math.pi / 180), 150 - 60 * math.sin((90 - hour_angle) * math.pi / 180))
    canvas.coords(minute_hand, 150, 150, 150 + 80 * math.cos((90 - minute_angle) * math.pi / 180), 150 - 80 * math.sin((90 - minute_angle) * math.pi/180 ))
    canvas.coords(second_hand, 150, 150, 150 + 90 * math.cos((90 - second_angle) * math.pi / 180), 150 - 80 * math.sin((90 - second_angle) * math.pi/180 ))
    canvas.config(background=colors[index])

    canvas.after(1000, update_clock)

root = tkinter.Tk()
root.title('Стрелочные часы')
canvas = tkinter.Canvas(root, width=300, height=300, background='red')
canvas.pack()
canvas.create_oval(50, 50, 250, 250)

hour_hand = canvas.create_line(150, 150, 150, 90, width=4, fill='white')
minute_hand = canvas.create_line(150, 150, 150, 70, width=3, fill='green')
second_hand = canvas.create_line(150, 150, 150, 60, width=3, fill='yellow')

canvas.create_text(150, 60, text='12', fill='black', font=('verdana', 12))
canvas.create_text(240, 150, text='3', fill='black', font=('verdana', 12))
canvas.create_text(150, 240, text='6', fill='black', font=('verdana', 12))
canvas.create_text(60, 150, text='9', fill='black', font=('verdana', 12))


update_clock()

root.mainloop()