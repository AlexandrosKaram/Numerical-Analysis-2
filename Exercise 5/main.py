import numpy as np
from random import uniform
from functions import lagrange, spline

# Range of values to generate [0, 2pi]
RANGE = (0, 2*np.pi)
# Decimal digit precision
PRECISION = 5


# Define main function
def main():
    # Generate 10 random numbers between 0 and 2pi
    x_values = [round(uniform(*RANGE), PRECISION) for i in range(10)]
    x_values.sort()

    # Calculate the sine of each value
    y_values = [round(np.sin(x), 5) for x in x_values]

    # Calculate the Lagrange results
    lagrange_results = lagrange(x_values, y_values)
    
    spline_function = spline(x_values, y_values)
    spline_results = [round(spline_function(x), PRECISION) for x in x_values]

    # Print results
    for i in range(len(x_values)):
        print(f"X: {x_values[i]}")
        print(f"Y: {y_values[i]}")
        print(f"Lagrange: {lagrange_results[i]}")
        print(f"Spline: {spline_results[i]}")
        print()


# Call main function
main()
