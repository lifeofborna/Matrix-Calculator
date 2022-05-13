from email import message
from tkinter import *
from tkinter import messagebox
from ui.ui import UserInterface
from services.user_service import UserService


class UserControl:

    '''
    This class handles and updates the login UI. 

    '''

    def __init__(self, root):
        self._root = root
        self._username = StringVar()
        self._password = StringVar()
        self._new_username = StringVar()
        self._new_password = StringVar()
        self._start = UserInterface()
        self._user_services = UserService()

        self.widgets()

    def create_user(self):
        create_user = self._user_services.create_user(
            self._new_username.get(), self._new_password.get())

        if create_user == True:
            messagebox.showinfo('Success!', 'Account has been created')
            self.log_frame()
        else:
            messagebox.showerror("Error", create_user)

    def login_user(self):
        '''
        login a user to the system
        '''
        login_user = self._user_services.login_user(
            self._username.get(), self._password.get())

        if login_user == True:
            self.login_frame.pack_forget()
            self._root.destroy()
            self._start.start(self._username.get())

        else:
            messagebox.showerror('Error', "No such credentials found")

    def log_frame(self):
        '''
        update login frame
        '''
        self._username.set('')
        self._password.set('')
        self.create_frame.pack_forget()
        self.head['text'] = 'Sign in'
        self.login_frame.pack()

    def reg_frame(self):
        '''
        update register frame
        '''
        self._new_username.set('')
        self._new_password.set('')
        self.login_frame.pack_forget()
        self.head['text'] = 'Sign up'
        self.create_frame.pack()

    def widgets(self):
        '''
        Create necessary widgets
        '''
        self.head = Label(self._root, text='Sign in',
                          font=('Raleway', 20), pady=10)
        self.head.pack()
        self.login_frame = Frame(self._root, padx=10, pady=10)
        Label(self.login_frame, text='Username: ', font=(
            'Raleway', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self._username,
              bd=5, font=('Raleway', 15)).grid(row=0, column=1)
        Label(self.login_frame, text='Password: ', font=(
            'Raleway', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self._password, bd=5,
              font=('Raleway', 15), show='*').grid(row=1, column=1)
        Button(self.login_frame, text=' Sign in ', bd=3, font=(
            'Raleway', 15), padx=5, pady=5, command=self.login_user).grid()
        Button(self.login_frame, text=' Sign Up ', bd=3, font=(
            'Raleway', 15), padx=5, pady=5, command=self.reg_frame).grid(row=2, column=1)
        self.login_frame.pack()

        self.create_frame = Frame(self._root, padx=10, pady=10)
        Label(self.create_frame, text='Username: ', font=(
            'Raleway', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_frame, textvariable=self._new_username,
              bd=5, font=('Raleway', 15)).grid(row=0, column=1)
        Label(self.create_frame, text='Password: ', font=(
            'Raleway', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_frame, textvariable=self._new_password, bd=5,
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
