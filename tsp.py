import random
import numpy as np


def generateElements(matrix, n):
    lower_bound = -10
    upper_bound = 10
    for i in range(0, n):
        for j in range(n - 1 - i, -1, -1):
            random_int = random.randint(lower_bound, upper_bound)
            matrix[i, j] = random_int
            matrix[j, i] = random_int

    return matrix


n = 5

matrix = np.empty((n, n), dtype=int)
matrix = generateElements(matrix, n)
