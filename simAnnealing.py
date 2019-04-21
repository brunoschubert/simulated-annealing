import numpy as np
from random import random, randint, choice
from readFiles import readFile
# ABSOLUTE PATH TO INSTANCES
test = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/test.col.txt"
games120 = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/games120.col.txt"  # 9
myciel6 = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/myciel6.col.txt"  # 7
anna = "D:/Unisinos/Inteligência Artificial/instâncias/GCP/anna.col.txt"  # 11

# MAIN PROGRAM


def colorGraph(file):
    # Define starting parameters
    file = file
    numColors = 12
    temperature = 1.0
    minTemperature = 0.0001
    alpha = 0.9
    steps = 100
    cost = 0
    # While the algorithm can reach a cost of zero
    # decreases the number of colors
    while(cost == 0):
        solution, cost = anneal(
            file, numColors, temperature, minTemperature, alpha, steps)
        if(cost == 0):
            numColors -= 1
    print("FINAL-> " + "Solution: " + str(solution) + " / " +
          " Cost: " + str(cost) + " / " + " Colors: " + str(numColors))


# ANNEALING ALGORITHM
def anneal(file, numColors, temperature, minTemperature, alpha, steps):
    adjMatrix, numVertices = readFile(file)
    numColors = numColors
    numColors -= 1
    temperature = temperature
    minTemperature = minTemperature
    alpha = alpha
    steps = steps
    solution = generateSolution(numVertices, numColors)
    cost, startNeighbour = checkCost(adjMatrix, solution)
    while temperature > minTemperature and cost != 0:
        i = 1
        while i <= steps:
            newSolution = genNeighbour(
                solution, numColors, numVertices, startNeighbour)
            newCost, startNeighbour = checkCost(
                adjMatrix, solution)
            ap = acceptance(cost, newCost, temperature)
            if ap > random():
                solution = newSolution
                cost = newCost
            i += 1
            print("Solution: " + str(solution) + " / " + " Cost: " +
                  str(cost) + " / " + " Color: " + str(numColors + 1) + " / " + " Temp: " + str(temperature))
        temperature = temperature*alpha
    numColors += 1
    return solution, cost

# Generate Acceptance Probability based on the function:
#  Acceptance = e*((newCost - oldCost) / Temperature)


def acceptance(oldCost, newCost, temperature):
    if newCost < oldCost:
        return 1
    else:
        ap = np.exp(- (newCost - oldCost) / temperature)
        return ap

# Calculates cost of the the solution based on the number of collisions
# and which collision to process


def checkCost(adjMatrix, solution):
    cost = 0
    collisionList = []
    neighbourIndex = -1
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix[i])):
            if(i != j and adjMatrix[i][j] == 1 and solution[i] == solution[j]):
                cost += 1
                collisionList.append(i)
    if(neighbourIndex == -1):
        prob = randint(1, 2)
        if(prob % 2 == 0 and len(collisionList) != 0):
            neighbourIndex = choice(collisionList)
        elif(1 < i < (len(adjMatrix)-1)):
            ap = randint(1, 3)
            if(ap % 3 == 0):
                neighbourIndex = choice(collisionList)
                neighbourIndex = neighbourIndex + prob
            elif(ap % 3 == 2):
                neighbourIndex = choice(collisionList)
                neighbourIndex = neighbourIndex - prob
            else:
                neighbourIndex = choice(len(solution))
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
# numColors = 16
# temperature = 1.0
# minTemperature = 0.0001
# alpha = 0.9
# steps = 100
# a, b, c = anneal(myciel6, numColors, temperature,
#                  minTemperature, alpha, steps)
# print("FINAL-> " + "Solution: " + str(a) + " / " +
#       " Cost: " + str(b) + " / " + " Colors: " + str(c))

colorGraph(anna)
