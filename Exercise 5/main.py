import numpy as np
from random import uniform
from functions import lagrange, spline, least_squares

# Range of values to generate [0, 2pi]
RANGE = (-np.pi, np.pi)
# Decimal digit precision
PRECISION = 8


# Define main function
def main():
    # Generate 10 random numbers between 0 and 2pi
    x_values = [round(uniform(*RANGE), PRECISION) for i in range(10)]
    x_values.sort()

    # Calculate the sine of each value
    y_values = [round(np.sin(x), PRECISION) for x in x_values]

    # Calculate the Lagrange results
    lagrange_results = lagrange(x_values, y_values)
    # Calculate the Spline results
    spline_results = spline(x_values, y_values)
    # Calculate the least squares results
    least_squares_results = least_squares(x_values, y_values)

    # Print results
    for i in range(len(x_values)):
        print(f"{i+1}.x: {x_values[i]}")
        print(f"Expected: {y_values[i]}, Lagrange: {lagrange_results[i]}, Spline: {spline_results[i]}, Least Squares: {least_squares_results[i]}")
        print()


# Call main function
main()
