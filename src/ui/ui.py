from email import message
import tkinter as tk
from typing import final
from unittest import result
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
#from matrixcalculator.matrix import matrix

from matrixcalculator.matrixlogic import MatrixLogic

# TODO Validation, If empty/wrong input set error,


class ui:
    def __init__(self):
        self.matrixOperations = MatrixLogic()

    def start(self):
        root = tk.Tk()
        root.resizable(False, False)
        canvas = tk.Canvas(root, width=500, height=300, bg="white")
        canvas.grid(columnspan=3, rowspan=3)

        # Matrix operations

        # Create a logo
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "LAMBDAB.png")
        logo = Image.open(open(data_file_path, 'rb'))
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(image=logo)
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

        # Create the matrix from the text variable
        def get_matrix(rows, cols, text_var):
            matrix = []

            for i in range(rows):
                matrix.append([])
                for j in range(cols):
                    try:
                        matrix[i].append(int(text_var[i][j].get()))
                    except:
                        messagebox.showerror(
                            "Error", "Please check matrix input!")
                        submit_text.set("Submit")
                        return

            return matrix

        # Operations:

        def addition():
            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)

            # Check if valid format before

            final_matrix = self.matrixOperations.matrix_addition(
                first_matrix, second_matrix)
            if final_matrix == False:
                return
            # Set result to resultant
            submit_text.set("Success!")
            resultant_matrix(final_matrix)

        def multiplication():
            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)
            try:
                final_matrix = self.matrixOperations.matrix_multiplication(
                    first_matrix, second_matrix)
            except:
                final_matrix = False

            # Check if valid format before
            if final_matrix == False:
                return
            submit_text.set("Success!")
            resultant_matrix(final_matrix)

        def substraction():
            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)

            final_matrix = self.matrixOperations.matrix_substraction(
                first_matrix, second_matrix)
            # Check if valid format before
            if final_matrix == False:
                return
            submit_text.set("Success!")
            resultant_matrix(final_matrix)

        def check_combo():
            first_matrix = get_matrix(3, 3, matrix_input)
            second_matrix = get_matrix(3, 3, matrix_input2)
            if chosen_operation.get() == ' Transpose matrix A':
                try:
                    final_matrix = self.matrixOperations.matrix_transpose(
                        second_matrix)
                except:
                    return
                resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Transpose matrix B':
                try:
                    final_matrix = self.matrixOperations.matrix_transpose(
                        first_matrix)
                except:
                    return
                resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Inverse matrix A':
                try:
                    final_matrix = self.matrixOperations.matrix_inverse(
                        second_matrix)
                except:
                    return
                if len(final_matrix) == 0:
                    messagebox.showerror(
                        "Warning", "Could not find an inverse for matrix A!")
                    return
                resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Inverse matrix B':
                try:
                    final_matrix = self.matrixOperations.matrix_inverse(
                        first_matrix)
                except:
                    return

                if len(final_matrix) == 0:
                    messagebox.showerror(
                        "Warning", "Could not find an inverse for matrix B!")
                    return
                resultant_matrix(final_matrix)

            elif chosen_operation.get() == ' Determinant A':
                try:
                    final_matrix = self.matrixOperations.matrix_determinant(
                        second_matrix)
                except:
                    return
                messagebox.showinfo(
                    "Info", f"The determinant for the matrix A is: {final_matrix}")

            elif chosen_operation.get() == " Determinant B":

                try:
                    final_matrix = self.matrixOperations.matrix_determinant(
                        first_matrix)
                except:
                    return
                messagebox.showinfo(
                    "Info", f"The determinant for the matrix B is: {final_matrix} ")

        # new canvas for matrixes
        canvas = tk.Canvas(root, width=500, height=250,)

        tk.Label(root, text="First Matrix :", font=('Raleway', 10, 'bold'),
                 bg="white").place(x=20, y=470)
        tk.Label(root, text="Second Matrix :", font=('Raleway', 10, 'bold'),
                 bg="white").place(x=155, y=470)
        tk.Label(root, text="Resultant Matrix :", font=('Raleway', 10, 'bold'),
                 bg="white").place(x=300, y=470)

        # In screen matrices:

        def entry_matrix(matrix_input, matrix_entries, s):
            # Create empty lists to array, append StringVar and entry
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

        # Create matrices
        entry_matrix(matrix_input, matrix_entries, 200)
        entry_matrix(matrix_input2, matrix_entries2, 50)
        resultant_matrix(final_matrix)

        # buttons
        submit_text = tk.StringVar()

        button = tk.Button(root, textvariable=submit_text, bg='DarkOliveGreen3',
                           width=7, command=lambda: get_matrix(3, 3, matrix_input))
        submit_text.set("Submit")
        button.place(x=200, y=600)

        button2 = tk.Button(root, textvariable=submit_text, bg='DarkOliveGreen3',
                            width=7, command=lambda: get_matrix(3, 3, matrix_input2))
        button2.place(x=50, y=600)

        multiplyButton = tk.Button(
            root, text="*", bg='DarkOliveGreen3', width=5, command=lambda: multiplication())
        multiplyButton.place(x=400, y=650)

        SubButton = tk.Button(
            root, text="-", bg='DarkOliveGreen3', width=5, command=lambda: substraction())
        SubButton.place(x=400, y=700)

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

        root.mainloop()
