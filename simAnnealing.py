import numpy as np

# Basic annealing function
# should separate parts in different helper functions
# as the basic values are defined


def anneal(solution,
           cost,
           random_neighbor,
           accept,
           T,
           T_min,
           alpha
           ):
  # INITIALIZE VARIABLES
  # Decides Starting cost based on Cost Function
    old_cost = cost(solution)
  # Defines Starting Temperature
    T = T
  # Defines lower Temperature threshold
    T_min = T_min
  # Lowers the overall temperature
    alpha = alpha
    # Starts the annealing process
    while T > T_min:
        i = 1
        while i <= 100:
          # Select a neighbor based on the cost
            new_solution = random_neighbor(solution)
            new_cost = cost(new_solution)
            # Decides if should accept or change based on Temperature and costs
            ap = accept(old_cost, new_cost, T)
            if ap > np.random():
                solution = new_solution
                old_cost = new_cost
            i += 1
        T = T*alpha
    return solution, cost

# -----------------PARAMENTER FUNCTIONS------------------


def cost():
  # Applies the cost function

    # TODO


def random_neighbor():
      # Generate a random neighbor/solutionution

        # TODO


def accept():
  # Decides if the algorithm should or not accept
  # the given solutionution based on a

    # TODO
