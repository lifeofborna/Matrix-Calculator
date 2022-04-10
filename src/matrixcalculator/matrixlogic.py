
from matrixcalculator.matrix import matrix


'''    
    This class has functions to calculate operations between two matrices.
    Such as,

    multiplication, addition and substraction

    
'''
class matrixlogic:


    #Addition of the two matrices.
    def additionOfMatrices(self, matrix1, matrix2):
        try:
            finalMatrix = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        except:
            return False
        return finalMatrix

    def substractionOfMatrices(self, matrix1, matrix2):
        try:
            finalMatrix = [[matrix1[i][j] - matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        except:
            return False
        return finalMatrix


    #Multiplication of two matrices.
    def matrixMultiplication(self,matrix1,matrix2):
        #Result will have same number of rows as first matrix, columns as second matrix->
        m = 3
        n = 3

        finalMatrix = [[ 0 for i in range(n) ] for j in range(m)]
        try:
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for m in range(len(matrix2)):
                        finalMatrix[i][j] += matrix1[i][m] * matrix2[m][j] 
        except:
            return False
        return finalMatrix