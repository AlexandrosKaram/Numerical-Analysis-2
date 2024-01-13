import numpy as np
from random import uniform
from functions import lagrange, spline, least_squares
from graph_error import display_error_graph

# Range of values to generate [-π, π]
RANGE = (-np.pi, np.pi)
# Decimal digit precision
PRECISION = 10


def result_difference(expected, method, precision=PRECISION):
    """Calculate the difference between the expected and the calculated result.
    
    Parameters:
        expected (float): Expected result
        method (float): Calculated result
    
    Returns:
        float: The average difference between the values of the two lists
    """
    difference = [round(abs(expected[i] - method[i]), precision) for i in range(len(expected))]
    return round(sum(difference)/len(difference), precision)


def get_x_values(n, value_range):
    """Generate n random x values in the given range.
    
    Parameters:
        n (int): Number of x values to generate
        value_range (tuple): Range of x values to generate
    
    Returns:
        list: List of generated x values
    """
    # Get n random values within the range
    result = [uniform(*value_range) for i in range(n)]
    result.sort()
    # Cover the whole range
    result[0] = value_range[0]
    result[-1] = value_range[1]

    return result

 
# Define main function
def main():
    # Generate 10 random numbers in our range to create our methods
    x_values = get_x_values(10, RANGE)
    # Calculate the sine of each value
    y_values = [round(np.sin(x), PRECISION) for x in x_values]

    # Generate 200 new x values to test our methods
    new_x_values = get_x_values(200, RANGE)
    new_y_values = [round(np.sin(x), PRECISION) for x in new_x_values]

    # Calculate the Lagrange results
    lagrange_results = lagrange(new_x_values, x_values, y_values)
    # Calculate the Spline results
    spline_results = spline(new_x_values, x_values, y_values)
    # Calculate the least squares results
    least_squares_results = least_squares(new_x_values, x_values, y_values)

    # Calculate the differences between the expected and the calculated results
    lagrange_difference = result_difference(new_y_values, lagrange_results)
    spline_difference = result_difference(new_y_values, spline_results)
    least_squares_difference = result_difference(new_y_values, least_squares_results)
    print("Average differences between the expected and the calculated results for each method:")
    print(f"\tLagrange: {lagrange_difference},\n\tSpline: {spline_difference},\n\tLeast squares: {least_squares_difference}")
    
    # Graph the errors between the expected and calculated results for each method
    display_error_graph(new_y_values, lagrange_results, new_x_values, "Lagrange")
    display_error_graph(new_y_values, spline_results, new_x_values, "Spline")
    display_error_graph(new_y_values, least_squares_results, new_x_values, "Least squares")


# Call main function
main()
