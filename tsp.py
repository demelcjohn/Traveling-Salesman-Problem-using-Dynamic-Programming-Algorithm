import random
import numpy as np
from display import display


def generateElements(matrix, n):
    lower_bound = 0
    upper_bound = 10
    for i in range(n):
        for j in range(i+1):
            if (i == j):
                matrix[i, j] = 0
                continue
            random_int = random.randint(lower_bound, upper_bound)
            matrix[i, j] = random_int
            matrix[j, i] = random_int

    return matrix


n = 5

matrix = np.empty((n, n), dtype=int)
matrix = generateElements(matrix, n)
display(matrix)
