

class matrix:
    '''
    Matrix class, idea is to format a string variable seperated with ";" ex: 123;123;123
    to a 
    matrix which is formatted to a array that consists of [[123],[123],[123]]

    Also functions to check if certain operations 
    
    '''
    def __init__(self, matrix, m,n):
        self.string = matrix


    def formatMatrix(self):
        matrix = []
        helper = []
        for i in self.string:
            if i == ";":
                matrix.append(helper)
                helper.clear()
                continue  
            helper.append(int(i))
        
        #if the matrix is empty but there is values in helper -> add them to matrix.
        #or there is values in helper -> add them to the matrix
        if len(matrix) == 0 or len(helper)>0:
            matrix.append(helper)

        return matrix


    #Check if matrix is legal
    def checkIfCorrectFormat(self):
        #Legal characters
        for i in self.string:
            if i.isdigit():
                if int(i) > 0:
                    continue            
            elif i == ";":
                continue            
            else:
                return False
        return True


    def __str__(self):
        return f"{self.string}"