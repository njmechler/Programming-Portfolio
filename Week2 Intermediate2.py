"""The following program, when executed will do several things. First, it will ask you for the dimensions of two matrices; one will be large
and one will be small. You decide the rows and columns for each, and, afterwards, you are left with a matrix of that size filled with integers from 0
to 9, all positive. Then(this is the important part), this program will take the smaller matrix and figure out if it can be found in the
bigger matrix. If it can, it will return YES, and, if it cannot, it will return NO."""

from random import *
def matrixProducer(rows, columns): #This generates a matrix with rows and columns specified by user, but random digits
    matrix =[]
    for i in xrange(rows):
        matrix.append([])
        for j in xrange(columns):
            matrix[i].append(randint(0,9))
    return matrix

def gridSearch(bigMatrix, smallMatrix):
    match = "NO"
    for i in xrange(len(bigMatrix)):
        for j in xrange(len(bigMatrix[0])):
             if (((len(bigMatrix) - i) >= len(smallMatrix)) and ((len(bigMatrix[0]) - (j)) >= len(smallMatrix[0])) and ((bigMatrix[i][j] == smallMatrix[0][0]))):
                testMatrix = []
                for key in xrange(len(smallMatrix)):
                    testMatrix.append([])
                for p in xrange(len(smallMatrix)):
                    for q in xrange(len(smallMatrix[0])):
                        testMatrix[p].append(bigMatrix[i + p][j + q])
                if (testMatrix == smallMatrix):
                    match = "YES"
                    return match
                    break
    return match


def grid_make_and_match():
    matrixLarge = matrixProducer(int(raw_input("How many rows in big Matrix?")), int(raw_input("How many columns in big Matrix?")))
    matrixSmall = matrixProducer(int(raw_input("How many rows in small Matrix?")), int(raw_input("How many columns in small Matrix?")))
    print(matrixLarge)
    print(matrixSmall)
    print(gridSearch(matrixLarge, matrixSmall))

print (grid_make_and_match())


                
    
    

    
