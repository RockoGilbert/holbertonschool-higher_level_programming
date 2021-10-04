#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    neo = []
    for x in matrix:
        neo.append(list(map(lambda num ** 2, x)))
    return (neo)
