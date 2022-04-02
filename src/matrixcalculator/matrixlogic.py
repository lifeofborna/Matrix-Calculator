
from matrixcalculator.matrix import matrix


'''
    This class takes 2 matrix objects, and calculates different operations. 
    additionOfMatrices takes 2 matrices and calculates the addition of each element in the matrix
    and return the matrix.
'''
class matrixlogic:

    #Check if correct dimension depending on the operation!
    def checkIfCorrectDimension(self,operation,n,m,n2,m2):
        
        if operation == "+" or operation == "-":
            if n == n2 and m == m2:return True 
     
        if operation == "*":
            if m == n2:return True
        
        return False


    #Addition of the two matrices.
    def additionOfMatrices(self, matrix1, matrix2):
        finalMatrix = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return finalMatrix

    def substractionOfMatrices(self, matrix1, matrix2):
        finalMatrix = [[matrix1[i][j] - matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return finalMatrix
