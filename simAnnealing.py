from random import random
from random import randint
import numpy as np
from readFiles import readFile

# TODO: Lower Colors Use
# TODO: Optimize Anneal

# ABSOLUTE PATH TO INSTANCES
# fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/test.col.txt"
# fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/games120.col.txt" #9
# fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/myciel6.col.txt" #7
fileToRead = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/anna.col.txt"  # 11

# ANNEALING ALGORITHM


def anneal(file):
    adjMatrix, numVertices = readFile(file)
    numColors = 15
    numColors -= 1
    T = 1.0
    T_min = 0.001
    alpha = 0.9
    steps = 100
    solution = generateSolution(numVertices, numColors)
    cost, startNeighbour = checkCost(adjMatrix, solution)
    while T > T_min and cost != 0:
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
            print("Solution: " + str(solution) + " / " + " Cost: " +
                  str(cost) + " / " + " Color: " + str(numColors) + " / " + " Temp: " + str(T))
        T = T*alpha
    return solution, cost, numColors

# Generate Acceptance Probability based on the function:
#  Acceptance = e*((newCost - oldCost) / Temperature)


def acceptance(oldCost, newCost, temperature):
    if newCost < oldCost:
        return 1
    else:
        p = np.exp((newCost - oldCost) / temperature)
        return p

# Calculates cost of the the solution based on the number of collisions


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

# Fill the solution array with random colors


def generateSolution(numVertices, numColors):
    solution = np.arange(numVertices)
    for i in range(numVertices):
        solution[i] = randint(0, numColors)
    return solution

# Generate a new neighbour solution


def genNeighbour(solution, numColors, numVertices, startNeighbour):
    oldColor = solution[startNeighbour]
    newColor = randint(0, numColors)
    while (oldColor == newColor):
        newColor = randint(0, numColors)
    solution[startNeighbour] = newColor
    return solution


# TESTS
a, b, c = anneal(fileToRead)
print("FINAL-> " + "Solution: " + str(a) + " / " +
      " Cost: " + str(b) + " / " + " Colors: " + str(c))
