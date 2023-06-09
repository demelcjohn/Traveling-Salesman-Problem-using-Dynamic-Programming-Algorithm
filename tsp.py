import copy
import random
import numpy as np
from display import display

n = 5

memo =  [[(-1, []) for _ in range(1 << n)] for _ in range(n)]

# print(memo)
# memoStack = [[[]]*(1 << (n)) for _ in range(n)]
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
    # print(i,mask,stack)
    if (mask & (~(1 << i))) == 1:
        memo[i][mask] = dist[i][0],stack
        # print("base cond:",i,mask,dist[i][0],stack)
        return dist[i][0],stack
    var,lst=memo[i][mask]
    if var != -1:
        # print("In var = :",i,mask,memo[i][mask])
        return memo[i][mask]

    resMin = 10**10
    stack2 = copy.copy(stack)
    for j in range(n):
        stack3 = []
        if (mask & (1 << j)) != 0 and j != i and j != 0:
            stack1 = copy.copy(stack2)
            res,stack1 = tspSolver(j, mask & (~(1 << i)),stack1)
            res = res +dist[i][j]
            stack3 = copy.copy(stack1)
            stack3.append(j)
            if resMin > res:
                resMin,stack = res,stack3

    memo[i][mask] = resMin,stack
    # print("full cond:",i,mask,memo[i][mask])
    return resMin,stack


# dist = np.empty((n, n), dtype=int)
# dist = generateElements(dist, n)

dist = [[0, 2, 5 ,7, 1],
[6, 0, 3, 8, 2],
[8, 7, 0, 4, 7],
[12, 4, 6, 0, 5],
[1, 3, 2, 8 ,0]]

dist = np.array(dist)
display(dist)

minCost = 10**10

stack = []
minStack.append(0)

for i in range(1,3):
    stack = []
    cost,stack = tspSolver(i, (1 << (n))-1,stack)
    stack.append(i)
    stack.append(0)
    cost = cost +dist[0][i]
    if minCost > cost:
        minCost,minStack = cost,stack
    # print(cost, stack)
print("The cost of most efficient tour = " + str(minCost))
print("The order of nodes : ",minStack)
# print(memo)
