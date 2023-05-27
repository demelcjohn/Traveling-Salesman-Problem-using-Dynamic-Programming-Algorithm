import random
import numpy as np
from display import display

n = 5

memo = [[-1]*(1 << (n)) for _ in range(n)]


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


def tspSolver(i, mask):

    if mask == 0:
        return dist[0][i]

    # if memo[i][mask] != -1:
    #     return memo[i][mask]

    res = 10**10

    for j in range(n):
        if (mask & (1 << j)) != 0 and j != i:
            res = min(res, tspSolver(j, mask & (~(1 << i))))
    return res


dist = np.empty((n, n), dtype=int)
dist = generateElements(dist, n)
display(dist)

cost = 10**10

for i in range(0, n):
    cost = min(cost, tspSolver(i, (1 << (n))-1))

print("The cost of most efficient tour = " + str(cost))
