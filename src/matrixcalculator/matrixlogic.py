
from matrixcalculator.matrix import matrix


'''    
    This class has functions to calculate operations between two matrices.
    Such as,

    multiplication, addition and substraction

    
'''
class matrixlogic:

    #Check if correct dimension depending on the operation!
    def checkIfCorrectDimension(self,operation,n,m,n2,m2):
        
        if operation == "+" or operation == "-":
            if n == n2 and m == m2:return True 

        #number of columns matrix1 has to equal numb of rows matrix2!
        if operation == "*":
            if n == m2:return True
        
        return False


    #Addition of the two matrices.
    def additionOfMatrices(self, matrix1, matrix2):
        finalMatrix = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return finalMatrix

    def substractionOfMatrices(self, matrix1, matrix2):
        finalMatrix = [[matrix1[i][j] - matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return finalMatrix


    #Multiplication of two matrices.
    def matrixMultiplication(self,matrix1,matrix2):
        #Result will have same number of rows as first matrix, columns as second matrix->
        m = len(matrix1)
        n = len(matrix2[0])

        finalMatrix = [[ 0 for i in range(n) ] for j in range(m)]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for m in range(len(matrix2)):
                    finalMatrix[i][j] += matrix1[i][m] * matrix2[m][j] 
        
        return finalMatrix