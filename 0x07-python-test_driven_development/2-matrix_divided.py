#!/usr/bin/python3
"""divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """Divides all elements"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for k in matrix:
            if len(i) != len(k):
                raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in row] for row in matrix]
