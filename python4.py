#tkinter

import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry('500x400')
root.title('Моя перваяпрограмма')
root.resizable(False, False)

#попробовать самостоятельно добавить иконку
#root.iconbitmap(default='favicon.ico') #.png, jpg -> ico

#виджеты
#button
click = 0
def start():
    global click
    click += 1
    #btn['text'] = 'Вы нажали на кнопку ' + str(click)
    btn['text'] = f'Вы нажали на кнопку {click}'


btn = ttk.Button(text='Зарегистрироваться', command=start)
btn.pack()

#Label
label1 = ttk.Label(text='Ваш логин:', font=('Verdana', 20))
label1.pack()
#установка изображений
#img = tkinter.PhotoImage(file='default.png') #самостоятельно скачать фото и проверить
#label2 = tkinter.Label(image=img)

root.iconbitmap(default='skype.ico')
#img = tkinter.PhotoImage(file='фото.png')

root.mainloop()