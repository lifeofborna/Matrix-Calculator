
'''
    This class has functions to calculate operations between two matrices.
    Such as,
    multiplication, addition and substraction    
'''


class MatrixLogic:

    # Addition of the two matrices.
    def matrix_addition(self, matrix1, matrix2):
        try:
            final_matrix = [[matrix1[i][j] + matrix2[i][j]
                             for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        except TypeError:
            return False
        return final_matrix

    def matrix_substraction(self, matrix1, matrix2):
        try:
            final_matrix = [[matrix1[i][j] - matrix2[i][j]
                             for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        except TypeError:
            return False
        return final_matrix

    # Multiplication of two matrices.
    def matrix_multiplication(self, matrix1, matrix2):
        # Result will have same number of rows as first matrix, columns as second matrix->
        columns = 3
        rows = 3
        final_matrix = [[0 for i in range(rows)] for j in range(columns)]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for columns in range(len(matrix2)):
                    if isinstance(matrix2[i][columns], int) \
                            and isinstance(matrix1[i][columns], int):
                        final_matrix[i][j] += matrix1[i][columns] * \
                            matrix2[columns][j]
                    else:
                        return False
        return final_matrix
