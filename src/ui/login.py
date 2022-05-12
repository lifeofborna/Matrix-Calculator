from email import message
from tkinter import *
from tkinter import messagebox
from venv import create
from ui.ui import UserInterface
from services.user_service import UserService


class UserControl:

    def __init__(self, root):
        self.root = root
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        self.start = UserInterface()
        self.user_services = UserService()

        self.widgets()

    def create_user(self):
        create_user = self.user_services.create_user(
            self.new_username.get(), self.new_password.get())

        if create_user == True:
            messagebox.showinfo('Success!', 'Account has been created')
            self.log_frame()
        else:
            messagebox.showerror("Error", create_user)

    def login_user(self):
        '''
        login a user to the system
        '''
        login_user = self.user_services.login_user(
            self.username.get(), self.password.get())

        if login_user == True:
            self.login_frame.pack_forget()
            self.root.destroy()
            self.start.start(self.username.get())

        else:
            messagebox.showerror('Error', "No such credentials found")

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
    UserControl(root)
    root.mainloop()
