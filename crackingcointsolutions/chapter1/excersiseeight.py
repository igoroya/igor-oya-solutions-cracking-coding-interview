'''
Created on 10 Aug 2017

Zero matrix: Write an algorithm such that if an element
in an MxN matix is 0, it's entire row and column are set to 0.

I assume that the matrix has integers types only

@author: igoroya
'''

def make_row_zeros(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def make_column_zeros(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0

def zero_matrix_s1(matrix):
    '''
    Matrix is represented as a nested list where i is the row and j is the column [i][j]

    In this solution, I use two auxiliary lists to hold the info if a column or a row has a zero.
    I loop over the matrix and find for which column or row should have zeros

    '''
    heigth = len(matrix)
    width = len(matrix[0])

    #create a matrix to remember if a column has a zero
    columns_zero = [False]*width
    rows_zero = [False]*heigth

    for i in range(heigth):
        for j in range(width):
            if matrix[i][j] is 0:
                columns_zero[j] = True
                rows_zero[i] = True

    #Implement the zeros:
    for i in range(heigth):
        if rows_zero[i]:
            make_row_zeros(matrix, i)

    for i in range(width):
        if columns_zero[i]:
            make_column_zeros(matrix, i)

    return matrix

def print_matrix(matrix):
    for i in matrix:
        print(i)
    print("")


if __name__ == '__main__':
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix_s1(matrix1))

    matrix1 = [[0, 2, 3, 1],
               [4, 5, 6, 1],
               [7, 8, 9, 1]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix_s1(matrix1))

    matrix1 = [[0, 2, 3, 1],
               [4, 5, 0, 1],
               [7, 8, 9, 1]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix_s1(matrix1))

    matrix1 = [[1, 2, 3, 1],
               [0, 5, 0, 1],
               [7, 8, 9, 1]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix_s1(matrix1))
    print("")









