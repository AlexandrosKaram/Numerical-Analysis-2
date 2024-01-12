import numpy as np
from random import uniform
from functions import lagrange

# Range of values to generate [0, 2pi]
RANGE = (0, 2*np.pi)


def main():
    # Generate 10 random numbers between 0 and 2pi
    x_values = [round(uniform(*RANGE), 5) for i in range(10)]
    x_values.sort()

    # Calculate the sine of each value
    expected_y_values = [round(np.sin(x), 5) for x in x_values]
    lagrange_results = [round(lagrange(x_values, expected_y_values, x), 5) for x in x_values]
    
    # Compare lagrange and expected results
    for i in range(len(lagrange_results)):
        print(f"For x={x_values[i]}, expected: {expected_y_values[i]}, Lagrange: {lagrange_results[i]}")


main()