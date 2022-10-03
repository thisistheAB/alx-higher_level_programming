#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    matrixLength = len(matrix)

    for matrixCounter in range(0, matrixLength):
        itemLength = len(matrix[matrixCounter])
        for itemCounter in range(0, itemLength):
            print('{:d}'.format(matrix[matrixCounter][itemCounter]), end=' ')
        if matrixCounter == matrixLength:
            break
        print('\n', end='')
