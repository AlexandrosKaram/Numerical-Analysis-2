import numpy as np
import matplotlib.pyplot as plt


def display_error_graph(expected_y, method_y, x_values, method_name):
    """Display a graph of the error between the expected and the calculated results.

    Parameters:
        expected_y (list): List of expected y values
        method_y (list): List of calculated y values
        x_values (list): List of x values
        method_name (str): Name of the method used
    """
    x_values = np.linspace(x_values[0], x_values[-1], len(expected_y))
    error_y_values = [abs(expected_y[i] - method_y[i]) for i in range(len(expected_y))]

    # Plot the function
    plt.figure()
    plt.plot(x_values, error_y_values)
    plt.grid()
    plt.title("Error graph of " + method_name + " method")
    plt.xlabel("x-ayis")
    plt.ylabel("Error")

    plt.show()