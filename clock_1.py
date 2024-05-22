import tkinter
import time
from tkinter import ttk

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)


a = tkinter.Tk()
a.title('Цифровые часы')
label = ttk.Label(a, font=('verdana', 40, 'bold'), background='purple', foreground='white')
label.pack()
update_time()
a.mainloop()