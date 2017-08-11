'''
Created on 10 Aug 2017

Zero matrix: Write an algorithm such that if an element
in an MxN matix is 0, it's entire row and column are set to 0.

I assume that the matrix has integers types only

@author: igoroya
'''

def zero_matrix(matrix):
    '''
    Matrix is represented as a nested list where i is the row and j is the column [i][j]
    '''
    heigth = len(matrix)
    width = len(matrix[0])



    skip_comumn = [False]*width

    for i in range(heigth):
        for j in range(width):
            if skip_comumn[j]:
                continue
            if matrix[i][j] is 0:
                skip_comumn[j] = True
                matrix[i] = [0]*width
                for k in range (heigth):
                    matrix[k][j] = 0
                break
    return matrix

def print_matrix(matrix):
    for i in matrix:
        print(i)

if __name__ == '__main__':
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix(matrix1))
    print("")

    matrix1 = [[0, 2, 3, 1],
               [4, 5, 6, 1],
               [7, 8, 9, 1]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix(matrix1))
    print("")

    matrix1 = [[0, 2, 3, 1],
               [4, 5, 0, 1],
               [7, 8, 9, 1]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix(matrix1))
    print("")

    matrix1 = [[1, 2, 3, 1],
               [4, 5, 0, 1],
               [7, 8, 9, 1]
        ]
    print_matrix(matrix1)
    print_matrix(zero_matrix(matrix1))
    print("")









