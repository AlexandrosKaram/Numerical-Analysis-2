# Functions used in exercise 5

import numpy as np
from helper import solve_linear_system


def lagrange(new_x_values, x_values, y_values):
    """Calculate the Lagrange polynomial.
    
    Parameters:
        new_x_values (list): List of new x values to calculate y values for
        x_values (list): List of x values
        y_values (list): List of y values

    Returns:
        tuple: The calculated y values
    """
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

    return tuple([sum(y_values[k]*lagrange_basis(x_values, x, k) for k in range(len(x_values))) for x in new_x_values])


def spline(new_x_values, x_values, y_values):
    """Calculate the spline polynomial.
    
    Parameters:
        new_x_values (list): List of new x values to calculate y values for
        x_values (list): List of x values
        y_values (list): List of y values

    Returns:
        tuple: The calculated y values
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
        return None  # Handle cases where x is outside the range of x_values (won't be needed as long as we cover the whole range in get_x_values()

    return tuple([spline_at(x) for x in new_x_values])


def least_squares(new_x_values, x_values, y_values):
    """Calculate results by the least squares method.
    
    Parameters:
        new_x_values (list): List of new x values to calculate y values for
        x_values (list): List of x values
        y_values (list): List of y values
    
    Returns:
        tuple: The calculated y values
    """
    n = len(x_values)

    # Calculate summations used in the least squares method
    sum_xy = sum(x_values[i]*y_values[i] for i in range(n)) 
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_x2 = sum(x_values[i]**2 for i in range(n))

    # Calculate m and b
    m = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)
    b = (sum_y - m*sum_x)/n

    # Implement linear regression formula (y = mx + b)
    return tuple([m*new_x_values[i] + b for i in range(len(new_x_values))])
