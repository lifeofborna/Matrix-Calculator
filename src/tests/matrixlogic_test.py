import unittest
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
