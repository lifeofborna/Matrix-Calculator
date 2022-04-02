
from matrixcalculator.matrix import matrix
from matrixcalculator.matrixlogic import matrixlogic

class ui:
    def __init__(self):
        self.matrixOperations = matrixlogic()
    

    def start(self):
        self.instructions()

        while True:
            inp = input("Enter a command: ")

            if inp == "0":
                print("You have decided to close the program. ")
                break
            
            #Addition
            if inp == "1":
                self.addition()            
                print("YAYYYYY")
                continue                
                


    def addition(self):

        size1 = input("Size of the first matrix (mxn): ")
        size2 = input("Size of the second matrix (mxn): ")
                
        if len(size1) != 3 or len(size2)!=3 or size1[1].isdigit() or size2[1].isdigit():
            print("Please use the right format for the sizes of the matrix")
            return 

        try:
            n = int(size1[0])
            m = int(size1[2])
            n2 = int(size2[0])
            m2 = int(size2[2])
        except:
            print("Please give valid size for the matrices!")
            
        if self.matrixOperations.checkIfCorrectDimension("+",n,m,n2,m2) == False:
            print("Dimensions mismatch! ")
            return

        matrix1 = matrix(input("Please give the first matrix!: "),n,m)
        matrix2 = matrix(input("Please give the second matrix!: "),n2,m2)

        if matrix1.checkIfCorrectFormat() == False:
            print(f"Please use the correct format for matrix: {matrix1}")
            return
                
        if matrix2.checkIfCorrectFormat() == False:
            print(f"Please use the correct format for matrix: {matrix2}")
            return
        
        matrix1 = matrix1.formatMatrix()
        matrix2 = matrix2.formatMatrix()

        print(f"Calculating {matrix1} + {matrix2} ")

        print(self.matrixOperations.additionOfMatrices(matrix1,matrix2))



    def instructions(self):
        print("Welcome to matrix calculator, 0 to stop, 1: for matrix addition")

        print("")

        print("Instructions: to give an matrix please use the following format: ")
        print("Seperate each row with a comma. eg: 123;123;123 for a 3x3 matrix with 123 as each row")  
        print("Dimensions of the matrix should be given in a mxn format! ")

        print("")
        return