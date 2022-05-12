import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import random
from time import strftime
import ui.login
from matrixcalculator.matrixlogic import MatrixLogic


class UserInterface:
    def __init__(self):
        self.matrixOperations = MatrixLogic()

    def start(self, username):
        root = tk.Tk()
        root.resizable(False, False)
        canvas = tk.Canvas(root, width=500, height=300, bg="white")
        canvas.grid(columnspan=3, rowspan=3)
        root.title("matrix calc")

        # Create a logo
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "LAMBDAB.png")
        logo = Image.open(open(data_file_path, 'rb'))
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

        # Empty variables for input
        matrix_input = []
        matrix_entries = []

        matrix_input2 = []
        matrix_entries2 = []

        rows, cols = 3, 3
        final_matrix = [[0] * rows for i in range(cols)]

        def show_error(first_matrix, second_matrix):
            if first_matrix == -1 and second_matrix == -1:
                messagebox.showerror("Error", "Please fill the matrices! ")
            elif first_matrix == -1:
                messagebox.showerror("Error", "Please fill the second matrix!")
            elif second_matrix == -1:
                messagebox.showerror("Error", "Please fill the first matrix!")

        def entry_matrix(matrix_input, matrix_entries, s):
            '''Creates empty lists to array and appends StringVar and entry'''

            x_interval = 0
            y_interval = 0
            rows, cols = (3, 3)
            for i in range(rows):
                matrix_input.append([])
                matrix_entries.append([])
                for j in range(cols):
                    matrix_input[i].append(tk.StringVar())
                    matrix_entries[i].append(
                        tk.Entry(root, textvariable=matrix_input[i][j], width=3))
                    matrix_entries[i][j].place(
                        x=s + x_interval, y=500 + y_interval)
                    x_interval += 30

                y_interval += 30
                x_interval = 0

        # Set the resultant matrix
        def resultant_matrix(resultantMatrix):
            '''Inserts a matrix to the resultant matrix'''
            s = 350
            x_interval = 0
            y_interval = 0
            rows, cols = (3, 3)
            for i in range(rows):
                for j in range(cols):
                    entry = tk.Entry(root, width=3)
                    entry.place(x=s + x_interval, y=500 + y_interval)
                    entry.insert(tk.END, resultantMatrix[i][j])
                    x_interval += 30
                y_interval += 30
                x_interval = 0

        def get_matrix(rows, cols, text_var):
            '''Creates a matrix from the values of the input

            Returns:
                A list containing lists which form a matrix.
            '''
            matrix = []

            for i in range(rows):
                matrix.append([])
                for j in range(cols):
                    try:
                        matrix[i].append(int(text_var[i][j].get()))
                    except:
                        return -1

            return matrix

        def clear_first_matrix():
            '''Clears the first matrix variables'''
            matrix_input.clear()
            matrix_entries.clear()

            entry_matrix(matrix_input, matrix_entries, 200)

        def clear_second_matrix():
            '''Clears the second matrix variables'''
            matrix_input2.clear()
            matrix_entries2.clear()

            entry_matrix(matrix_input2, matrix_entries2, 50)

        def addition():
            '''Initializes matrix addition by getting two matrix inputs,
               calling matrixlogic class for matrix addition with the matrices. 
            '''
            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)

            if first_matrix == -1 or second_matrix == -1:
                show_error(first_matrix, second_matrix)

            else:
                final_matrix = self.matrixOperations.matrix_addition(
                    first_matrix, second_matrix)

                resultant_matrix(final_matrix)

        def multiplication():
            '''Initializes matrix multiplication by getting two matrix inputs,
               calling matrixlogic class for matrix multiplication function with the matrices. 
            '''

            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)

            if first_matrix == -1 or second_matrix == -1:
                show_error(first_matrix, second_matrix)
            else:
                final_matrix = self.matrixOperations.matrix_multiplication(
                    first_matrix, second_matrix)
                resultant_matrix(final_matrix)

        def substraction():
            '''Initializes matrix substraction by getting two matrix inputs,
               calling matrixlogic class for matrix addition with the matrices. 
            '''

            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)

            if first_matrix == -1 or second_matrix == -1:
                show_error(first_matrix, second_matrix)

            else:
                final_matrix = self.matrixOperations.matrix_substraction(
                    first_matrix, second_matrix)
                resultant_matrix(final_matrix)

        def check_combo():
            '''Checks which extra operation is chosen and calls the appropriate function 
            from matrixlogic'''

            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)

            if chosen_operation.get() == ' Transpose matrix A':
                if second_matrix == -1:
                    show_error(first_matrix, second_matrix)

                else:

                    final_matrix = self.matrixOperations.matrix_transpose(
                        second_matrix)

                    resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Transpose matrix B':
                if first_matrix == -1:
                    show_error(first_matrix, second_matrix)

                else:
                    final_matrix = self.matrixOperations.matrix_transpose(
                        first_matrix)

                resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Inverse matrix A':
                if second_matrix == -1:
                    show_error(first_matrix, second_matrix)
                else:
                    final_matrix = self.matrixOperations.matrix_inverse(
                        second_matrix)

                    if len(final_matrix) == 0:
                        messagebox.showerror(
                            "Warning", "Could not find an inverse for matrix A!")
                    else:
                        resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Inverse matrix B':
                if first_matrix == -1:
                    show_error(first_matrix, second_matrix)

                else:

                    final_matrix = self.matrixOperations.matrix_inverse(
                        first_matrix)

                    if len(final_matrix) == 0:
                        messagebox.showerror(
                            "Warning", "Could not find an inverse for matrix B!")
                    else:
                        resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Determinant A':
                if second_matrix == -1:
                    show_error(first_matrix, second_matrix)
                else:

                    final_matrix = self.matrixOperations.matrix_determinant(
                        second_matrix)

                    messagebox.showinfo(
                        "Info", f"The determinant for the matrix A is: {final_matrix}")

            elif chosen_operation.get() == " Determinant B":
                if first_matrix == -1:
                    show_error(first_matrix, second_matrix)
                else:
                    final_matrix = self.matrixOperations.matrix_determinant(
                        first_matrix)

                    messagebox.showinfo(
                        "Info", f"The determinant for the matrix B is: {final_matrix} ")

        # new canvas for matrixes
        canvas = tk.Canvas(root, width=500, height=250,)

        def matrix_labels():
            '''defines matrix labels'''

            tk.Label(root, text="First Matrix :", font=('Raleway', 10, 'bold'),
                     bg="white").place(x=20, y=470)
            tk.Label(root, text="Second Matrix :", font=('Raleway', 10, 'bold'),
                     bg="white").place(x=155, y=470)
            tk.Label(root, text="Resultant Matrix :", font=('Raleway', 10, 'bold'),
                     bg="white").place(x=300, y=470)

        def logout():
            '''Logs out the user and opens the login view'''
            question = messagebox.askquestion(
                'Exit Application', "Are you sure you wish to logout?")
            if question == "yes":

                root.destroy()
                quit()
                root2 = tk.Tk()
                root2.title('Login Form')
                ui.login.UserControl(root2)
                root2.mainloop()

            else:
                messagebox.showinfo(
                    "Return", "You will be returned back to the calculator")

        def time():
            '''Creates time label and places it'''
            time_label = tk.Label(root, font=("Raleway", 10, 'bold'),
                                  background="SlateBlue2",
                                  foreground="white")

            string = strftime('%H:%M:%S %p')
            time_label.config(text=string)
            time_label.place(x=185, y=45)

            root.after_id = time_label.after(1000, time)

        def welcome_username():
            tk.Label(root, text=f"Welcome ", font=('Raleway', 10, 'bold'),
                     bg="white", fg="SlateBlue2").place(x=175, y=20)
            user_label = tk.Label(root, text=f"{username}", font=('Raleway', 10, 'bold'),
                                  bg="white")

            colors = ["SlateBlue3", "SlateBlue4",
                      "RoyalBlue1", "tomato", "SlateBlue2", "sandy brown", "light pink", "turquoise", "dodger blue"]
            fg = random.choice(colors)
            user_label.config(fg=fg)

            user_label.place(x=250, y=20)

            root.after_id = user_label.after(3000, welcome_username)

        def initialize():
            '''Initializes the welcome,time label and sets the entry matrices'''
            if len(username) < 8 and len(username) >= 1:
                welcome_username()
            else:
                tk.Label(root, text=f"Welcome user", font=('Raleway', 10, 'bold'),
                         bg="white", fg="SlateBlue2").place(x=175, y=20)

            time()
            entry_matrix(matrix_input, matrix_entries, 200)
            entry_matrix(matrix_input2, matrix_entries2, 50)
            resultant_matrix(final_matrix)
            matrix_labels()

        def quit():
            """Cancel all scheduled callbacks and quit."""
            for after_id in root.tk.eval('after info').split():
                root.after_cancel(after_id)

        # buttons
        cleared_text = tk.StringVar()
        cleared_text2 = tk.StringVar()
        button = tk.Button(root, textvariable=cleared_text, bg='DarkOliveGreen3',
                           width=7, command=lambda: clear_first_matrix())
        cleared_text.set("clear")
        button.place(x=200, y=600)

        button2 = tk.Button(root, textvariable=cleared_text2, bg='DarkOliveGreen3',
                            width=7, command=lambda: clear_second_matrix())
        cleared_text2.set("clear")
        button2.place(x=50, y=600)

        multiplyButton = tk.Button(
            root, text="*", bg='DarkOliveGreen3', width=5, command=lambda: multiplication())
        multiplyButton.place(x=400, y=650)

        SubButton = tk.Button(
            root, text="-", bg='DarkOliveGreen3', width=5, command=lambda: substraction())
        SubButton.place(x=400, y=700)

        logout_button = tk.Button(
            root, text="logout", bg='SlateBlue2', width=3, height=1, command=lambda: logout())
        logout_button.place(x=200, y=75)

        additionButton = tk.Button(
            root, text="+", bg='DarkOliveGreen3', width=5, command=lambda: addition())
        additionButton.place(x=400, y=600)

        combo_box_button = tk.Button(
            root, text="get", bg='DarkOliveGreen3', width=5, command=lambda: check_combo())
        combo_box_button.place(x=30, y=720)

        # Extra operations
        n = tk.StringVar()
        chosen_operation = ttk.Combobox(width=15, textvariable=n)

        # Dropdownlist for combobox
        tk.Label(root, text="Extra operations:", font=('Raleway', 10, 'bold'),
                 ).place(x=23, y=660)

        chosen_operation['values'] = (' Determinant A', ' Determinant B', ' Inverse matrix A',
                                      ' Inverse matrix B', ' Transpose matrix A', ' Transpose matrix B')
        chosen_operation.place(x=30, y=690)

        canvas.grid(columnspan=3)

        initialize()

        root.mainloop()
