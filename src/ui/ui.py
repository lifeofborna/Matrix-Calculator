
from matrixcalculator.matrix import matrix
from matrixcalculator.matrixlogic import matrixlogic

##TODO Fix values over 9 for example if user inserts values 23 23 -> they should be seperate
##TODO 
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
                continue                
            
            if inp == "2":
                self.substraction()
                continue
    
            if inp == "3":
                self.multiplication()
                continue
    
    def multiplication(self):
        matrix1,matrix2 = self.getMatrix("*")
        if matrix1 == False or matrix2 == False:
            return 
        
        print(f"Calculating {matrix1} * {matrix2} ")

        print(self.matrixOperations.matrixMultiplication(matrix1,matrix2))


    def substraction(self):
        matrix1,matrix2 = self.getMatrix("-")
        if matrix1 == False or matrix2 == False:
            return 
        
        print(f"Calculating {matrix1} - {matrix2} ")

        print(self.matrixOperations.substractionOfMatrices(matrix1,matrix2))


    def addition(self):
        matrix1,matrix2 = self.getMatrix("+")
        if matrix1 == False or matrix2 == False:
            return 
        
        print(f"Calculating {matrix1} + {matrix2} ")
        
        print("")

        print(self.matrixOperations.additionOfMatrices(matrix1,matrix2))



    def checkRightFormat(self,size1, size2, operation):

        if len(size1) != 3 or len(size2)!=3 or size1[1].isdigit() or size2[1].isdigit():
            print("Please use the right format for the sizes of the matrix")
            return False

        try:
            n = int(size1[0])
            m = int(size1[2])
            n2 = int(size2[0])
            m2 = int(size2[2])
            
        except:
            print("Please give valid size for the matrices!")
            return False
        

        if self.matrixOperations.checkIfCorrectDimension(operation,n,m,n2,m2) == False:
            print("Dimensions mismatch! ")
            return False



        return True


    def sizeOfMatrices(self):
        size1 = input("Size of the first matrix (mxn): ")
        size2 = input("Size of the second matrix (mxn): ")
                
        return size1,size2



    def getMatrix(self, operation):
        size1, size2 = self.sizeOfMatrices()

        if not self.checkRightFormat(size1,size2,operation):
            return False, False

        n = int(size1[0])
        m = int(size1[2])
        n2 = int(size2[0])
        m2 = int(size2[2])
            
        
        matrix1 = matrix(input("Please give the first matrix!: "),n,m)
        matrix2 = matrix(input("Please give the second matrix!: "),n2,m2)


        if matrix1.checkIfCorrectFormat() == False:
            print(f"Please use the correct format for matrix: {matrix1}")
            return False, False
                
        if matrix2.checkIfCorrectFormat() == False:
            print(f"Please use the correct format for matrix: {matrix2}")
            return False, False
        

        matrix1 = matrix1.formatMatrix()
        matrix2 = matrix2.formatMatrix()

        if matrix1 == -1 or matrix2 == -1:
            print("""There occurred an error in the matrices you inserted,
            please use correct form!""")
            return False, False
        
        return matrix1,matrix2


    def instructions(self):
        print("""Welcome to matrix calculator! 
        0: To exit the program 
        1: for matrix addition 
        2: for matrix substraction
        3: for matrix multiplication
        """)

        print("")

        print(""" Instructions: 

                  To give an matrix please use the following format: 

                  Seperate each row with a " ; ". 
                  eg:  1 1 1;1 1 1;1 1 1;
                  for a :
                       
                      1 1 1
                      1 1 1
                      1 1 1

                    matrix.  
                               
                  
                  Dimensions of the matrix should be given in a mxn format!                                                  """)

        print("")
        return