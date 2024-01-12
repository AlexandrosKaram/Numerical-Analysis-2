import numpy as np
from random import uniform

# Range of values to generate [0, 2pi]
RANGE = (0, 2*np.pi)


def lagrange_basis(x_values, x, k):
    """Calculate the Lagrange basis polynomial.
    
    Parameters:
        x_values (list): List of x values
        x (float): The x value to calculate the Lagrange basis polynomial for
        k (int): The index of the Lagrange basis polynomial
    Returns:
        float: The Lagrange basis polynomial for the given x value
    """
    return np.prod([(x - x[j])/(x[k] - x[j]) for j in range(len(x_values)) if j != k])


def lagrange(x_values, y_values, x):
    """Calculate the Lagrange polynomial.
    
    Parameters:
        x_values (list): List of x values
        y_values (list): List of y values
        x (float): The x value to calculate the Lagrange polynomial for

    Returns:
        float: The Lagrange polynomial for the given x value
    """
    return sum(y_values[k]*lagrange_basis(x_values, x, k) for k in range(len(x_values)))


def main():
    # Generate 10 random numbers between 0 and 2pi
    x_values = [round(uniform(*RANGE), 5) for i in range(10)]
    x_values.sort()
    # Calculate the sine of each value
    expected_y_values = [round(np.sin(x), 5) for x in x_values]


        


main()