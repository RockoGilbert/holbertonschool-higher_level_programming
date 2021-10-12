#!/usr/bin/python
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of matrix by "div"
    checks if all of matrix is int/float
    checks if each list in matrix are the same size
    checks if "div" is an int/float or is 0
    """
    Err0 = "matrix must be a matrix (list of lists) of integers/floats"
    Err1 = "Each row of the matrix must have the same size"
    newMatrix = []
    
    if not isinstance(div, (int, float)):
        raise TypeError ("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError ("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(Err1)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(Err0)
            else:
                inner_list.append(round(items / div, 2))
        newMatrix.append(inner_list)
        
    return newMatrix
