import unittest
from matrixcalculator.matrixlogic import matrixlogic



class TestMatrixLogic(unittest.TestCase):
    def setUp(self):
        self.matrixLogic = matrixlogic() 

    def test_check_if_correct_dimension_with_operator_addition(self):
        operation = "+"
        n = 2
        m = 3
        n2 = 2
        m2 = 3

        answer =  self.matrixLogic.checkIfCorrectDimension(operation,n,m,n2,m2)

        self.assertEqual(str(answer),"True")
    
    def test_check_if_not_correct_dimension_with_operator_addition(self):
        operation = "+"
        n = 2
        m = 3
        n2 = 2
        m2 = 1

        answer =  self.matrixLogic.checkIfCorrectDimension(operation,n,m,n2,m2)

        self.assertEqual(str(answer),"False")
    
    def test_check_if_correct_dimension_with_operator_multiply(self):
        operation = "*"
        n = 2
        m = 3
        n2 = 3
        m2 = 2

        answer =  self.matrixLogic.checkIfCorrectDimension(operation,n,m,n2,m2)

        self.assertEqual(str(answer),"True")

    
    def test_check_if_not_correct_dimension_with_operator_multiply(self):
        operation = "*"
        n = 2
        m = 3
        n2 = 2
        m2 = 3

        answer =  self.matrixLogic.checkIfCorrectDimension(operation,n,m,n2,m2)

        self.assertEqual(str(answer),"False")
