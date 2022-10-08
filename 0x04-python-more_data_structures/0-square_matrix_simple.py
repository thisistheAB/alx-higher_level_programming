#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    squareMatrix = []
    listsInMatrix = len(matrix)

    for currentList in range(0, listsInMatrix):
        currentListLength = len(matrix[currentList])
        currentListSquared = []
        for currentItemIndex in range(0, currentListLength):
            currentItem = matrix[currentList][currentItemIndex]
            currentItemSquared = currentItem ** 2
            currentListSquared.append(currentItemSquared)
        squareMatrix.append(currentListSquared)

    return squareMatrix
