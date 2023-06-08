import copy
import random
import numpy as np
from display import display

n = 4

memo = [[-1]*(1 << (n)) for _ in range(n)]
minStack = []


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


def tspSolver(i, mask,stack):
    if (mask & (~(1 << i))) == 1:
        return dist[i][0],stack
    # if memo[i][mask] != -1:
    #     return memo[i][mask]

    resMin = 10**10
    stack2 = copy.copy(stack)
    for j in range(n):
        if (mask & (1 << j)) != 0 and j != i and j != 0:
            stack1 = copy.copy(stack2)
            stack1.append(j)
            res,stack1 = tspSolver(j, mask & (~(1 << i)),stack1)
            res = res +dist[i][j]
            if resMin > res:
                resMin,stack = res,stack1

    memo[i][mask] = res
    return resMin,stack


# dist = np.empty((n, n), dtype=int)
# dist = generateElements(dist, n)

dist = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
dist = np.array(dist)
display(dist)

minCost = 10**10

stack = []
minStack.append(0)

for i in range(1, n):
    stack = [0]
    stack.append(i)
    cost,stack = tspSolver(i, (1 << (n))-1,stack)
    cost = cost +dist[0][i]
    if minCost > cost:
        minCost,minStack = cost,stack
    print(minCost, minStack)
print("The cost of most efficient tour = " + str(minCost))
print(minStack)
