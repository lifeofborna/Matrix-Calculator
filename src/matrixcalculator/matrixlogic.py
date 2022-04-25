
import numpy as np


class MatrixLogic:

    '''
    This class has functions to calculate operations between two matrices.
    Such as,
    multiplication, addition and substraction.
    It can also produce a inverse, determinant or transpose of a matrix
    '''
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

    # Find the determinant by cofactor
    def matrix_determinant(self, matrix):
        matrix_a = matrix[0][0]
        matrix_b = matrix[0][1]
        matrix_c = matrix[0][2]

        determinant_a = matrix_a * \
            (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        determinant_b = -matrix_b * \
            (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
        determinant_c = matrix_c * \
            (matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])

        answer = determinant_a+determinant_b+determinant_c
        return answer

    # Transpose the matrix rows = cols
    def matrix_transpose(self, matrix):
        matrix_transpose = [[1 for i in range(3)] for j in range(3)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix_transpose[j][i] = matrix[i][j]
        return matrix_transpose

    # Find the inverse of the matrix, utilizing numpy
    def matrix_inverse(self, matrix):
        if self.matrix_determinant(matrix) == 0:
            return []

        create_matrix = np.array(matrix)
        inverse_matrix = np.linalg.inv(create_matrix)
        inverse_matrix.round(decimals=2)
        return inverse_matrix
