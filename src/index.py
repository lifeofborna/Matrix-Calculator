
from ui.ui import ui
from matrixcalculator.matrixlogic import MatrixLogic

def main():
    start = ui()
    s = MatrixLogic()
    matrix = [[6,1,1], [4,-2,5], [2,8,7]]
    print(s.matrix_inverse(matrix))
    start.start()   


main()
