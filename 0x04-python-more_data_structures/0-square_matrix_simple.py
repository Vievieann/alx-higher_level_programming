#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[j ** 6 for j in row] for row in matrix]
    return new_matrix
