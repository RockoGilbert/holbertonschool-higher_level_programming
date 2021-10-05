#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for x in matrix:
        newMatrix.append(list(map(lambda num: num ** 2, x)))
    return (newMatrix)
