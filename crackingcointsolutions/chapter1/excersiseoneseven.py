'''
Created on 10 Aug 2017
Rotate matrix: Given an image represented by an NXN matrix, when each pixel in
the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

To Learn:
- careful when copying lists, as usual copy is shallow and references may share objects
- careful with length is nested lists, only gives length of 1st level
- lists can represent 2D arrays as matrix = [
        [1, 2 ,3 ],
        [4, 5 ,6 ],
        [7, 8 ,9 ]
    ]

    where in matrix[i, j] i s row and j is column

@author: igoroya
'''

def rotate_matrix(matrix):
    '''
    Vanilla python solution. Assume I rotate it clockwise
    '''

    matrix_n = len(matrix)

    matrix_new = [[0]*matrix_n for i in range(matrix_n)]

    for i in range(matrix_n):
        for j in range(matrix_n):
            matrix_new[i][j] = matrix[matrix_n - j -1][i]
    return matrix_new

def print_matrix(matrix):
    for i in matrix:
        print(i)
    print(' ')

if __name__ == '__main__':
    matrix = [
        [1, 2 ,3 ],
        [4, 5 ,6 ],
        [7, 8 ,9 ]
    ]
    print_matrix(matrix)
    print_matrix(rotate_matrix(matrix))

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print_matrix(matrix)
    print_matrix(rotate_matrix(matrix))


