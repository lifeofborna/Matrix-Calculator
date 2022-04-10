import tkinter as tk
from typing import final
from unittest import result
from PIL import Image,ImageTk
from soupsieve import select
from tkinter.filedialog import askopenfile
from tkinter import ttk

#from matrixcalculator.matrix import matrix

from matrixcalculator.matrixlogic import matrixlogic

#TODO Validation, If empty/wrong input set error,

class tt:
    def __init__(self):
        self.matrixOperations = matrixlogic()

    def start(self): 
        root = tk.Tk()
        root.resizable(False,False)
        canvas = tk.Canvas(root,width=500,height=300,bg="white")
        canvas.grid(columnspan=3,rowspan=3)

        ##Matrix operations
    

        #Create a logo 
        logo = Image.open(open("ui/LAMBDAB.png",'rb'))
        logo = ImageTk.PhotoImage(logo)
        logo_label= tk.Label(image=logo)
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1,row=0)


        # Empty variables for input
        matrix_input = []
        matrix_entries = []

        matrix_input2 = []
        matrix_entries2 = []

        rows, cols = 3, 3
        finalMatrix = [[0] * rows for i in range(cols)]

        # Create the matrix from the text variable
        def get_matrix(rows,cols,text_var):
            matrix = []

            for i in range(rows):
                matrix.append([])
                for j in range(cols):
                    try:
                        matrix[i].append(int(text_var[i][j].get()))
                    except:
                        submitText.set("Check input")
                        return

            
            return matrix

        
        
        #Operations: 

        def addition():
            firstMatrix = get_matrix(3,3,matrix_input)
            secondMatrix = get_matrix(3,3,matrix_input2)

            #Check if valid format before

            finalMatrix = self.matrixOperations.additionOfMatrices(firstMatrix,secondMatrix)
            if finalMatrix == False:
                return
            #Set result to resultant
            submitText.set("Success!")
            resultantMatrix(finalMatrix)

        
        def multiplication():
            firstMatrix = get_matrix(3,3,matrix_input)
            secondMatrix = get_matrix(3,3,matrix_input2)
        
            finalMatrix = self.matrixOperations.matrixMultiplication(firstMatrix,secondMatrix)
            #Check if valid format before
            if finalMatrix == False:
                return
            submitText.set("Success!")
            resultantMatrix(finalMatrix)

        def substraction():
            firstMatrix = get_matrix(3,3,matrix_input)
            secondMatrix = get_matrix(3,3,matrix_input2)

            
            finalMatrix = self.matrixOperations.substractionOfMatrices(firstMatrix,secondMatrix)
            #Check if valid format before
            if finalMatrix == False:
                return
            submitText.set("Success!")
            resultantMatrix(finalMatrix)





        ##new canvas for matrixes
        canvas = tk.Canvas(root,width=500,height=250,)

        tk.Label(root, text="First Matrix :", font=('Raleway', 10, 'bold'), 
            bg="white").place(x=20, y=470)
        tk.Label(root, text="Second Matrix :", font=('Raleway', 10, 'bold'), 
            bg="white").place(x=155, y=470)
        tk.Label(root, text="Resultant Matrix :", font=('Raleway', 10, 'bold'), 
            bg="white").place(x=300, y=470)

        
        #In screen matrices:


        def entryMatrix(matrix_input,matrix_entries,s):
            #Create empty lists to array, append StringVar and entry
            x_interval = 0
            y_interval = 0
            rows, cols = (3,3)
            for i in range(rows):
                matrix_input.append([])
                matrix_entries.append([])
                for j in range(cols):
                    matrix_input[i].append(tk.StringVar())
                    matrix_entries[i].append(tk.Entry(root, textvariable=matrix_input[i][j],width=3))
                    matrix_entries[i][j].place(x=s + x_interval, y=500 + y_interval)
                    x_interval += 30

                y_interval += 30
                x_interval = 0

        #Set the resultant matrix
        def resultantMatrix(resultantMatrix):
            s = 350
            x_interval = 0
            y_interval = 0
            rows,cols = (3,3)
            for i in range(rows):
                for j in range(cols):
                    entry = tk.Entry(root, width=3)
                    entry.place(x=s + x_interval, y=500 + y_interval)
                    entry.insert(tk.END, resultantMatrix[i][j])
                    x_interval+=30
                y_interval += 30
                x_interval = 0
            


        #Create matrices
        entryMatrix(matrix_input,matrix_entries,200)
        entryMatrix(matrix_input2,matrix_entries2,50)
        resultantMatrix(finalMatrix)


        #buttons
        submitText = tk.StringVar()
        
        button= tk.Button(root,textvariable=submitText, bg='DarkOliveGreen3', width=7, command=lambda:get_matrix(3,3,matrix_input))
        submitText.set("Submit")
        button.place(x=200,y=600)

        button2= tk.Button(root,textvariable=submitText, bg='DarkOliveGreen3', width=7, command=lambda:get_matrix(3,3,matrix_input2))
        button2.place(x=50,y=600)

        multiplyButton= tk.Button(root,text="*", bg='DarkOliveGreen3', width=5, command=lambda:multiplication())
        multiplyButton.place(x=400,y=650)

        SubButton= tk.Button(root,text="-", bg='DarkOliveGreen3', width=5, command=lambda:substraction())
        SubButton.place(x=400,y=700)

        additionButton= tk.Button(root,text="+", bg='DarkOliveGreen3', width=5, command=lambda:addition())
        additionButton.place(x=400,y=600)


        canvas.grid(columnspan=3)

        root.mainloop()
