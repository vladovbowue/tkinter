from tkinter import *
root = Tk()
root.title('Canvas')
root.geometry('300x300')

canvas = Canvas(bg='white', width=250, height=250)
canvas.pack(anchor=CENTER, expand=1)
canvas.create_line(10, 10, 200, 50, width=10, fill='red',dash=True)


canvas.create_rectangle(10, 20, 200, 60, fill='yellow', outline='#004D40', width=10)
# #004D40
#   r g b
#0 1 2 3 4 5 6 7 8 9 a b c d e f

canvas.create_oval(10, 10, 200, 50, fill='green', outline='blue',width=10)

#canvas.create_polygon(10, 30, 200, 200, 200, 30, fill='#80CBC4')

#список [3,5,3,2,10]
#кортеж (45,12,45,1)

points = (
    (10, 30),
    (200, 200),
    (200, 30)
)
canvas.create_polygon(*points, fill='#80CBC4')


canvas.create_arc((10, 10), (200, 200), fill='red')

canvas.create_text(50, 50, text='Мой текст', fill='black', font=('Tahoma', 15))

#img = PhotoImage(file='default.png') проверить
#canvas.create_image(10, 10, image=img)

root.mainloop()