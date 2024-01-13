# Functions used in exercise 5

import numpy as np
from helper import solve_linear_system


def lagrange_basis(x_values, x, k):
    """Calculate the Lagrange basis polynomial.
    
    Parameters:
        x_values (list): List of x values
        x (float): The x value to calculate the Lagrange basis polynomial for
        k (int): The index of the Lagrange basis polynomial
    Returns:
        float: The Lagrange basis polynomial for the given x value
    """
    return np.prod([(x - x_values[j])/(x_values[k] - x_values[j]) for j in range(len(x_values)) if j != k])


def lagrange(x_values, y_values):
    """Calculate the Lagrange polynomial.
    
    Parameters:
        x_values (list): List of x values
        y_values (list): List of y values

    Returns:
        tuple: The Lagrange polynomial 
    """
    return tuple([sum(y_values[k]*lagrange_basis(x_values, x, k) for k in range(len(x_values))) for x in x_values])


def spline(x_values, y_values):
    """Calculate the spline polynomial.
    
    Parameters:
        x_values (list): List of x values
        y_values (list): List of y values

    Returns:
        function: A function that computes the spline polynomial for a given x value
    """
    a = []   # α
    delta = []   # δ
    Delta = []   # Δ

    # Calculate α, δ and Δ
    for i in range(len(x_values) - 1):
        a.append(y_values[i])
        delta.append((x_values[i + 1] - x_values[i]))
        Delta.append((y_values[i + 1] - y_values[i]))

    # Calculate coefficient matrix 
    matrix = np.zeros((len(x_values), len(x_values)))
    matrix[0][0] = 1
    matrix[-1][-1] = 1
    for i in range(1, len(x_values) - 1):
        matrix[i][i] = 2*(delta[i - 1] + delta[i])
        matrix[i][i - 1] = delta[i - 1]
        matrix[i][i + 1] = delta[i]
    
    # Calculate right hand side vector
    vector = np.zeros(len(x_values))
    vector[0] = vector[-1] = 0
    for i in range(1, len(x_values) - 1):
        vector[i] = 3*(Delta[i]/delta[i] - Delta[i - 1]/delta[i - 1])

    # Solve linear system for c
    c = solve_linear_system(matrix.tolist(), vector.tolist())

    # Calculate d and b
    d = []
    b = []
    for i in range(len(x_values) - 1):
        d.append((c[i + 1] - c[i])/(3*delta[i]))
        b.append(Delta[i]/delta[i] - delta[i]*(2*c[i] + c[i + 1])/3)
    
    # Define a function to calculate the spline polynomial for a given x
    def spline_polynomial(i, x):
        dx = x - x_values[i]
        return a[i] + b[i]*dx + c[i]*(dx**2) + d[i]*(dx**3)

    # Define a function that interpolates between the data points
    def spline_at(x):
        for i in range(len(x_values) - 1):
            if x_values[i] <= x <= x_values[i + 1]:
                return spline_polynomial(i, x)
        return None  # Handle cases where x is outside the range of x_values

    return spline_at
