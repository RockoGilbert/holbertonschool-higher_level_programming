#!/usr/bin/python3
"""This Module returns a list of lists of integers
    representing the Pascal’s triangle of n
    """


def pascal_triangle(n):
    """Returns lists to represent Pascal's triangle"""

    if n <= 0:
        return []

    result = []
    tmpList = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(tmpList[j] + tmpList[j - 1])
        tmpList = row
        result.append(row)
    return result
