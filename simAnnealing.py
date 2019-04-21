from random import random
from random import randint
import numpy as np
from readFiles import readFile

# TODO: Check While loops
# TODO: Lower Colors Use
# TODO: Optimize Anneal
# TODO: Check why annel is getting stuck at indexes
# TODO: Change at both indexes?

# fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/test.col.txt"
fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/games120.col.txt"


def anneal(file):
    adjMatrix, numVertices = readFile(file)
    numColors = 20
    numColors -= 1
    T = 1.0
    T_min = 0.001
    alpha = 0.9
    steps = 10
    solution = generateSolution(numVertices, numColors)
    cost, startNeighbour = checkCost(adjMatrix, solution)
    while T > T_min:
        i = 1
        while i <= steps:
            newSolution = genNeighbour(
                solution, numColors, numVertices, startNeighbour)
            newCost, startNeighbour = checkCost(
                adjMatrix, solution)
            ap = acceptance(cost, newCost, T)
            if ap > random():
                solution = newSolution
                cost = newCost
            i += 1
            print("Solution: " + str(solution) + " / " + " Cost: " + str(cost))
        T = T*alpha
    return solution, cost

# Generate Acceptance Probability based on the function:
#  Acceptance = e*((newCost - oldCost) / Temperature)


def acceptance(oldCost, newCost, temperature):
    if newCost < oldCost:
        return 1
    else:
        p = np.exp((newCost - oldCost) / temperature)
        return p


def checkCost(adjMatrix, solution):
    cost = 0
    neighbourIndex = -1
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix[i])):
            if(i != j and adjMatrix[i][j] == 1 and solution[i] == solution[j]):
                cost += 1
                if(neighbourIndex == -1):
                    prob = randint(1, 2)
                    if(prob % 2 == 0):
                        neighbourIndex = i
                    elif(1 < i < (len(adjMatrix)-1)):
                        ap = randint(1, 10)
                        if(ap % 2 == 0):
                            neighbourIndex = i + prob
                        else:
                            neighbourIndex = i - prob
    return cost, neighbourIndex

# Se na matriz marcar 1, olha na posição da solução pra ver se tem conflito


def generateSolution(numVertices, numColors):
    solution = np.arange(numVertices)
    for i in range(numVertices):
        solution[i] = randint(0, numColors)
    return solution


def genNeighbour(solution, numColors, numVertices, startNeighbour):
    oldColor = solution[startNeighbour]
    newColor = randint(0, numColors)
    while (oldColor == newColor):
        newColor = randint(0, numColors)
    solution[startNeighbour] = newColor
    return solution


def check(numVertices):
    for vert in range(numVertices):
        print(vert)


# TESTS
a, b = anneal(fileToRead)
print("FINAL-> " + "Solution: " + str(a) + " / " + " Cost: " + str(b))
