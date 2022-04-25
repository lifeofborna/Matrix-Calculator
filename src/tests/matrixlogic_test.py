import unittest

from numpy import transpose

from matrixcalculator.matrixlogic import MatrixLogic


class TestMatrixLogic(unittest.TestCase):
    def setUp(self):
        self.matrixLogic = MatrixLogic()

    def test_check_if_matrix_addition_is_false(self):
        rows = 3
        columns = 3
        matrix1 = [[2 for i in range(rows)] for j in range(columns)]
        matrix2 = [['a' for i in range(rows)] for j in range(columns)]

        finalMatrix = self.matrixLogic.matrix_addition(matrix1, matrix2)

        self.assertEqual(str(finalMatrix), "False")

    def test_check_if_matrix_addition_is_correct(self):
        rows = 3
        columns = 3
        matrix1 = [[1 for i in range(rows)] for j in range(columns)]
        matrix2 = [[1 for i in range(rows)] for j in range(columns)]

        finalMatrix = self.matrixLogic.matrix_addition(matrix1, matrix2)
        correct_answer = [[2 for i in range(rows)] for j in range(columns)]

        self.assertEqual(finalMatrix, correct_answer)

    def test_check_if_matrix_substraction_is_false(self):
        rows = 3
        columns = 3
        matrix1 = [[2 for i in range(rows)] for j in range(columns)]
        matrix2 = [['a' for i in range(rows)] for j in range(columns)]

        finalMatrix = self.matrixLogic.matrix_substraction(matrix1, matrix2)

        self.assertEqual(str(finalMatrix), "False")

    def test_check_if_matrix_addition_is_correct(self):
        rows = 3
        columns = 3
        matrix1 = [[1 for i in range(rows)] for j in range(columns)]
        matrix2 = [[1 for i in range(rows)] for j in range(columns)]

        finalMatrix = self.matrixLogic.matrix_substraction(matrix1, matrix2)
        correct_answer = [[0 for i in range(rows)] for j in range(columns)]

        self.assertEqual(finalMatrix, correct_answer)

    def test_check_if_matrix_multiplication_is_false(self):
        rows = 3
        columns = 3
        matrix1 = [[2 for i in range(rows)] for j in range(columns)]
        matrix2 = [['a' for i in range(rows)] for j in range(columns)]

        finalMatrix = self.matrixLogic.matrix_multiplication(matrix1, matrix2)

        self.assertEqual(str(finalMatrix), "False")

    def test_check_if_matrix_multiplication_is_correct(self):
        rows = 3
        columns = 3
        matrix1 = [[1 for i in range(rows)] for j in range(columns)]
        matrix2 = [[1 for i in range(rows)] for j in range(columns)]

        finalMatrix = self.matrixLogic.matrix_multiplication(matrix1, matrix2)
        correct_answer = [[3 for i in range(rows)] for j in range(columns)]

        self.assertEqual(finalMatrix, correct_answer)

    def test_check_if_matrix_determinant_is_correct(self):
        rows = 3
        columns = 3
        matrix1 = [[1 for i in range(rows)] for j in range(columns)]

        finalMatrix = self.matrixLogic.matrix_determinant(matrix1)
        correct_answer = 0

        self.assertEqual(finalMatrix, correct_answer)

    def test_check_if_matrix_inverse_is_correct(self):
        matrix1 = [[1, 2, -1], [2, 1, 2], [-1, 2, 1]]
        finalMatrix = self.matrixLogic.matrix_inverse(matrix1)
        answer = [[0.1875, 0.25, -0.3125],
                  [0.25, 0.0, 0.25], [-0.3125, 0.25, 0.1875]]

        ans = answer[0][0]
        compare = finalMatrix[0][0]

        self.assertEqual(ans, compare)

    def test_check_if_matrix_transpose_is_correct(self):
        matrix1 = [[2, 2, 2], [1, 1, 1], [1, 1, 1]]
        transpose_matrix1 = [[2, 1, 1], [2, 1, 1], [2, 1, 1]]

        finalMatrix = self.matrixLogic.matrix_transpose(matrix1)

        self.assertEqual(finalMatrix, transpose_matrix1)
