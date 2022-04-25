from tkinter import *
from tkinter import messagebox
import sqlite3
from ui.ui import ui

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()


cursor.execute(
    'CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL);')
db.commit()
db.close()


class userControl:

    def __init__(self, root):
        self.root = root
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        self.start = ui()

        self.widgets()

    def create_user(self):
        '''
        create a new user into database

        '''
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()

        taken_user = ('SELECT username FROM User WHERE username = ?')
        cursor.execute(taken_user, [(self.new_username.get())])
        found_user = cursor.fetchall()

        if found_user or self.new_username == "":
            messagebox.showerror(
                'Error', 'Selected Username is not unique, please try again!')
            return
        else:
            messagebox.showinfo('Success!', "Account has been created!")
            self.log_frame()

        create_account = 'INSERT INTO user(username,password) VALUES(?,?)'
        cursor.execute(create_account, [
                       (self.new_username.get()), (self.new_password.get())])
        db.commit()

    def login_user(self):
        '''
        login a user to the system
        '''
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()

        search_user = (
            'SELECT * FROM user WHERE username = ? AND password = ?')
        cursor.execute(
            search_user, [(self.username.get()), (self.password.get())])
        res = cursor.fetchall()

        if res:
            self.login_frame.pack_forget()
            self.root.destroy()
            self.start.start()

        else:
            messagebox.showerror('Error', "No such username found")

    def log_frame(self):
        '''
        update login frame
        '''
        self.username.set('')
        self.password.set('')
        self.create_frame.pack_forget()
        self.head['text'] = 'Sign in'
        self.login_frame.pack()

    def reg_frame(self):
        '''
        update register frame
        '''
        self.new_username.set('')
        self.new_password.set('')
        self.login_frame.pack_forget()
        self.head['text'] = 'Sign up'
        self.create_frame.pack()

    def widgets(self):
        '''
        Create necessary widgets
        '''
        self.head = Label(self.root, text='Sign in',
                          font=('Raleway', 20), pady=10)
        self.head.pack()
        self.login_frame = Frame(self.root, padx=10, pady=10)
        Label(self.login_frame, text='Username: ', font=(
            'Raleway', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self.username,
              bd=5, font=('Raleway', 15)).grid(row=0, column=1)
        Label(self.login_frame, text='Password: ', font=(
            'Raleway', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self.password, bd=5,
              font=('Raleway', 15), show='*').grid(row=1, column=1)
        Button(self.login_frame, text=' Sign in ', bd=3, font=(
            'Raleway', 15), padx=5, pady=5, command=self.login_user).grid()
        Button(self.login_frame, text=' Sign Up ', bd=3, font=(
            'Raleway', 15), padx=5, pady=5, command=self.reg_frame).grid(row=2, column=1)
        self.login_frame.pack()

        self.create_frame = Frame(self.root, padx=10, pady=10)
        Label(self.create_frame, text='Username: ', font=(
            'Raleway', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_frame, textvariable=self.new_username,
              bd=5, font=('Raleway', 15)).grid(row=0, column=1)
        Label(self.create_frame, text='Password: ', font=(
            'Raleway', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_frame, textvariable=self.new_password, bd=5,
              font=('Raleway', 15), show='*').grid(row=1, column=1)
        Button(self.create_frame, text='Create Account', bd=3, font=(
            'Raleway', 15), padx=5, pady=5, command=self.create_user).grid()
        Button(self.create_frame, text='return', bd=3, font=('Raleway', 15),
               padx=5, pady=5, command=self.log_frame).grid(row=2, column=1)


def run_class():
    root = Tk()
    root.title('Login Form')
    userControl(root)
    root.mainloop()
