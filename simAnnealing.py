from random import random
from random import randint
import numpy as np

# TODO: Integrate Graph Coloring problem into algorithm {Define temperatures, steps, etc}
# TODO: Define final Cost function
# TODO: Modularize code
# TODO: Probabilistically decrease Temperature
# TODO: Check While loops

# TODO: Colors Vector
# TODO: Cost as amount of Collisions

fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/test.col.txt"
# fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/games120.col.txt"


def anneal(starter):
    sol = neighbor_solution(starter)
    old_cost = calculate_cost(sol)
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    steps = 1000
    while T > T_min:
        i = 1
        while i <= steps:
            new_sol = neighbor_solution(sol)
            new_cost = calculate_cost(new_sol)
            ap = acceptance(old_cost, new_cost, T)
            if ap > random():
                sol = new_sol
                old_cost = new_cost
            i += 1
            print("Solution: " + str(sol) + " / " + " Cost: " + str(old_cost))
        T = T*alpha
    return sol, old_cost

# Generate Acceptance Probability based on the function:
#  Acceptance = e*((cost_new - cost_old) / Temperature)


def acceptance(cost_old, cost_new, Temp):
    if cost_new < cost_old:
        return 1
    else:
        p = np.exp(- (cost_new - cost_old) / Temp)
        # print(str(p))
        return p


def checkCost(adjMatrix, solution, numVertices):
    for vert in range(numVertices):
        cost = 0
        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix[i])):
                if(adjMatrix[i][j] == 1 and solution[vert] == solution[i]):
                    cost += 1
    return cost

# Se na matriz marcar 1, olha na posição da solução pra ver se tem conflito


def generateSolution(solution, numVertices, numColors):
    for i in range(numVertices):
        solution[i] = randint(0, numColors)
    return solution


# TESTS
a, b = anneal(100)
print("FINAL-> " + "Solution: " + str(a) + " / " + " Cost: " + str(b))
