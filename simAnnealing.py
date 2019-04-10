from random import random
import numpy as np

# TODO: Integrate Graph Coloring problem into algorithm {Define temperatures, steps, etc}
# TODO: Define final Cost function
# TODO: Modularize code
# TODO: Probabilistically decrease Temperature
# TODO: Check While loops


def anneal(starter):
    sol = neighbor_solution(starter)
    old_cost = calculate_cost(sol)
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    steps = 5
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

# Defines cost based on current solution


def calculate_cost(sol):
    a = sol ** 2
    # print(str(a))
    return a

# Generate Random Neighbor Solution


def neighbor_solution(sol):
    sol = sol * random()
    # print(sol)
    return sol


a, b = anneal(10)
print("FINAL-> " + "Solution: " + str(a) + " / " + " Cost: " + str(b))
