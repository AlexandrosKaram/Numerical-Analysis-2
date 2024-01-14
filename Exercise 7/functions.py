import numpy as np


def least_squares_2(new_x_values, x_values, y_values):
    """Calculate the least squares method for a second degree polynomial.

    Parameters:
        new_x_values (list): List of x values to calculate the polynomial for
        x_values (list): List of x values
        y_values (list): List of y values

    Returns:
        list: List of y values for the calculated polynomial
    """
    # Summations needed for the calculation
    sum_x = np.sum(x_values)
    sum_y = np.sum(y_values)
    sum_x2 = np.sum([x**2 for x in x_values])
    sum_x3 = np.sum([x**3 for x in x_values])
    sum_x4 = np.sum([x**4 for x in x_values])
    sum_xy = np.sum([x*y for x, y in zip(x_values, y_values)])
    sum_x2y = np.sum([x**2*y for x, y in zip(x_values, y_values)])
    
    n = len(x_values)

    # Calculate the coefficients
    coefficient_matrix = np.array([[sum_x4, sum_x3, sum_x2],
                      [sum_x3, sum_x2, sum_x],
                      [sum_x2, sum_x, n]])
    vector = np.array([sum_x2y, sum_xy, sum_y])

    # Using numpy to solve the system of equations 
    a, b, c = np.linalg.solve(coefficient_matrix, vector)

    # Calculate the y values for the new x values
    return [a*x**2 + b*x + c for x in new_x_values]