

class matrix:
    '''
    Matrix class, idea is to format the input given by the user
    to a matrix that can be used to calculate the operations.

    Class also checks if the input is legal for the operations. 
    
    '''
    def __init__(self, matrix, m,n):
        self.string = matrix
        self.n = n
        self.m = m


    def formatMatrix(self):
        matrix = []
        helper = []
        value = ""

        #If " " --> concatenate numbers to a one number
        for i in self.string:
            if i == " " and value == "":
                continue
            
            if i == " ":
                    helper.append(int(value))
                    value = ""
                    return -1

            if i == ";":
                if value != "":
                    helper.append(int(value))
                
                matrix.append(helper[:])
                helper.clear()
                value = ""
                continue  
            
            if value == "":
                value = i
            else:
                value+=i

        #if the matrix is empty but there is values in helper -> add them to matrix.
        #or there is values in helper -> add them to the matrix
        if len(matrix) == 0 or len(helper)>0 or value != "":
            matrix.append(helper)

         
       # print(matrix)
        if not self.checkIfMatrixIsCorrectSize(matrix,self.m,self.n):
            return -1

        return matrix


    #Check if matrix is legal
    def checkIfCorrectFormat(self):
        #Legal characters
        for i in self.string:
            if i.isdigit():
                if int(i) >= 0:
                    continue            
            elif i == ";":
                continue
            elif i == " ":
                continue            
            else:
                return False

        return True


    #Check if the matrix is actually mxn!
    def checkIfMatrixIsCorrectSize(self,matrix1,m,n):
        if len(matrix1) != m:return False
        
        for i in matrix1:
            if len(i) != n:
                return False
        return True


    def __str__(self):
        return f"{self.string}"