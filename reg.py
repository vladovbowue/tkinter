import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

def reg():
    pol = value.get()
    login = login_txt.get()
    password = password_txt.get()
    if login == '' or password == '':
        showerror('Ошибка', 'Ошибка ввода логина и / или пароля')
    else:
        showinfo("Успешная Регистрация","Вы успешно зарегестрированы")
        f = open('users.txt', 'a') #a - режим дозаписи
        #f.write(f'login: {login} password: {password}')
        if pol == 1:
            b = 'Мужской'
        else:
            b = 'Женский'
        f.write('\nlogin: ' + login + ' password: *' + password + '* Пол: ' + b)
        f.close()
def auth():
    def auth_def():
        password = password_2.get()
        f = open('users.txt', 'r')
        users_1 = f.readlines()
        print(users_1)

    b = tkinter.Tk()
    b.title('Авторизация')
    h2 = ttk.Label(b, text='Авторизация', font=('Verdana', 20), padding=10)
    h2.grid(row=0, column=0, columnspan=2)

    password_2_l = ttk.Label(b, text='Password: ', font=('Verdana', 13), padding=10)
    password_2_l.grid(row=1, column=0)

    password_2 = ttk.Entry(b, width=45, show='*')
    password_2.grid(row=1, column=1)

    btn_2_auth = ttk.Button(b, text='Войти', command=auth_def)
    btn_2_auth.grid(row=2, column=0, columnspan=2)

a = tkinter.Tk()
a.iconbitmap(default='skype.ico')
a.title('Регистрация')
a.geometry('400x300')
h1 = ttk.Label(text='Регистрация',font=('Verdana', 20),padding=10)
h1.grid(row=0, column=0, columnspan=2)

login_l = ttk.Label(text='Login: ',font=('Verdana', 13), padding=10)
login_l.grid(row=1, column=0)

login_txt =ttk.Entry(width=45)
login_txt.grid(row=1, column=1)


password_l = ttk.Label(text='Password: ',font=('Verdana', 13), padding=10)
password_l.grid(row=2, column=0)

password_txt = ttk.Entry(width=45, show='*')
password_txt.grid(row=2, column=1)

value = tkinter.IntVar()
check_1 = ttk.Checkbutton(text='Муж.', variable=value)
check_1.grid(row=3, column=0)



btn_reg = ttk.Button(text='Регистрация', command=reg)
btn_reg.grid(row=3, column=1)
btn_auth = ttk.Button(text='Авторизация', command=auth)
btn_auth.grid(row=4, column=1)

a.mainloop()