import numpy as np

def trapezoidal_integration(x_range):
    range_diff = x_range[-1] - x_range[0]
    N = 10   # Number of intervals (11 - 1)

    # Calculate x values
    x_values = np.array([x_range[0] + i * range_diff / N for i in range(N+1)])
    # Calculate y values
    y_values = np.sin(x_values)

    return range_diff / (2 * N) * (y_values[0] + y_values[-1] + 2 * np.sum(y_values[1:-1])) 
    

def simpson_integration(x_range):
    range_diff = x_range[-1] - x_range[0]
    N = 10   # Number of intervals (11 - 1)

    # Calculate x values
    x_values = np.array([x_range[0] + i * range_diff / N for i in range(N+1)])
    # Calculate y values
    y_values = np.sin(x_values)
    
    return range_diff / (3 * N) * (y_values[0] + y_values[-1] + 2 * np.sum(y_values[2: -1: 2]) + 4 * np.sum(y_values[1: -1: 2]))
