#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix = map(lambda x: x * x, matrix)
    return (new_matrix)
