import numpy as np
from random import uniform
from functions import lagrange, spline, least_squares

# Range of values to generate [0, 2pi]
RANGE = (-np.pi, np.pi)
# Decimal digit precision
PRECISION = 5


def print_results(x_values, expected_y, method_y):
    """Print the results of the calculations.

    Parameters:
        x_values (list): List of x values
        expected_y (list): List of expected y values
        method_y (list): List of calculated y values
    """
    for i in range(len(x_values)):
        print(f"{i+1}. For x={x_values[i]}:")
        print(f"\tExpected: {expected_y[i]},\n\tMethod: {method_y[i]}")

 
# Define main function
def main():
    # Generate 10 random numbers in our range
    x_values = [uniform(*RANGE) for i in range(10)]
    x_values.sort()

    # Calculate the sine of each value
    y_values = [np.sin(x) for x in x_values]

    # Generate new x values to test our methods
    new_x_values = [uniform(*RANGE) for i in range(10)]
    new_x_values.sort()
    new_y_values = [np.sin(x) for x in new_x_values]

    # Calculate the Lagrange results
    lagrange_results = lagrange(new_x_values, x_values, y_values)
    # Calculate the Spline results
    spline_results = spline(new_x_values, x_values, y_values)
    # Calculate the least squares results
    least_squares_results = least_squares(new_x_values, x_values, y_values)

    # Print results
    print("Calculated y values using the following methods:")
    print("Lagrange:")
    print_results(new_x_values, new_y_values, lagrange_results)
    print()
    print("Spline:")
    print_results(x_values, y_values, spline_results)
    print()
    print("Least squares:")
    print_results(x_values, y_values, least_squares_results)
    print()


# Call main function
main()
