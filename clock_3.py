import tkinter
import time
from tkinter import ttk
#pygame
t = 60
def update_timer():
    global t
    t = t - 1
    timer.config(text=str(t))
    timer.after(1000, update_timer)

a=tkinter.Tk()
a.title("таймер")
timer=ttk.Label(a, font=('verdana', 40, 'bold'))
timer.pack()


update_timer()

a.mainloop()