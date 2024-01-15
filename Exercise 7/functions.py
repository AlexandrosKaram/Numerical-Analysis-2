import numpy as np


def least_squares_2(new_x_values, x_values, y_values):
    """Calculate y for the new x values using the least squares method for a second degree polynomial.
    
    Parameters:
        new_x_values (list): List of x values to calculate y for
        x_values (list): List of x values
        y_values (list): List of y values
    
    Returns:
        tuple: List of y values for the new x values
    """
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    # Summations needed for the calculation
    sum_x = np.sum(x_values)
    sum_y = np.sum(y_values)
    sum_x2 = np.sum(x_values**2)
    sum_x3 = np.sum(x_values**3)
    sum_x4 = np.sum(x_values**4)
    sum_xy = np.sum(x_values * y_values)
    sum_x2y = np.sum(x_values**2 * y_values)
    
    n = len(x_values)

    # Calculate the coefficients
    coefficient_matrix = np.array([[sum_x4, sum_x3, sum_x2],
                      [sum_x3, sum_x2, sum_x],
                      [sum_x2, sum_x, n]])
    vector = np.array([sum_x2y, sum_xy, sum_y])

    # Using numpy to solve the system of equations 
    a, b, c = np.linalg.solve(coefficient_matrix, vector)

    # Calculate the y values for the new x values
    return tuple([a*x**2 + b*x + c for x in new_x_values])


def least_squares_3(new_x_values, x_values, y_values):
    """Calculate y for the new x values using the least squares method for a third degree polynomial.

    Parameters:
        new_x_values (list): List of x values to calculate y for
        x_values (list): List of x values
        y_values (list): List of y values
    
    Returns:
        tuple: List of y values for the new x values
    """
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    # Summations needed for the calculation
    sum_x = np.sum(x_values)
    sum_y = np.sum(y_values)
    sum_x2 = np.sum(x_values**2)
    sum_x3 = np.sum(x_values**3)
    sum_x4 = np.sum(x_values**4)
    sum_x5 = np.sum(x_values**5)
    sum_x6 = np.sum(x_values**6)
    sum_xy = np.sum(x_values * y_values)
    sum_x2y = np.sum(x_values**2 * y_values)
    sum_x3y = np.sum(x_values**3 * y_values)

    n = len(x_values)

    # Calculate the coefficients
    coefficient_matrix = np.array([[sum_x6, sum_x5, sum_x4, sum_x3],
                      [sum_x5, sum_x4, sum_x3, sum_x2],
                      [sum_x4, sum_x3, sum_x2, sum_x],
                      [sum_x3, sum_x2, sum_x, n]])
    vector = np.array([sum_x3y, sum_x2y, sum_xy, sum_y])

    a, b, c, d = np.linalg.solve(coefficient_matrix, vector)

    # Calculate the y values for the new x values
    return tuple([a*x**3 + b*x**2 + c*x + d for x in new_x_values])


def least_squares_4(new_x_values, x_values, y_values):
    """Calculate y for the new x values using the least squares method for a fourth degree polynomial.
    
    Parameters:
        new_x_values (list): List of x values to calculate y for
        x_values (list): List of x values
        y_values (list): List of y values

    Returns:
        tuple: List of y values for the new x values
    """
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    # Summations needed for the calculation
    sum_x = np.sum(x_values)
    sum_y = np.sum(y_values)
    sum_x2 = np.sum(x_values**2)
    sum_x3 = np.sum(x_values**3)
    sum_x4 = np.sum(x_values**4)
    sum_x5 = np.sum(x_values**5)
    sum_x6 = np.sum(x_values**6)
    sum_x7 = np.sum(x_values**7)
    sum_x8 = np.sum(x_values**8)
    sum_xy = np.sum(x_values * y_values)
    sum_x2y = np.sum(x_values**2 * y_values)
    sum_x3y = np.sum(x_values**3 * y_values)
    sum_x4y = np.sum(x_values**4 * y_values)

    n = len(x_values)

    # Calculate the coefficients
    coefficient_matrix = np.array([[sum_x8, sum_x7, sum_x6, sum_x5, sum_x4],
                      [sum_x7, sum_x6, sum_x5, sum_x4, sum_x3],
                      [sum_x6, sum_x5, sum_x4, sum_x3, sum_x2],
                      [sum_x5, sum_x4, sum_x3, sum_x2, sum_x],
                      [sum_x4, sum_x3, sum_x2, sum_x, n]])
    vector = np.array([sum_x4y, sum_x3y, sum_x2y, sum_xy, sum_y])

    a, b, c, d, e = np.linalg.solve(coefficient_matrix, vector)

    # Calculate the y values for the new x values
    return tuple([a*x**4 + b*x**3 + c*x**2 + d*x + e for x in new_x_values])
