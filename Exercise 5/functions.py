# Functions used in exercise 5


def lagrange_basis(x_values, x, k):
    """Calculate the Lagrange basis polynomial.
    
    Parameters:
        x_values (list): List of x values
        x (float): The x value to calculate the Lagrange basis polynomial for
        k (int): The index of the Lagrange basis polynomial
    Returns:
        float: The Lagrange basis polynomial for the given x value
    """
    return np.prod([(x - x_values[j])/(x_values[k] - x_values[j]) for j in range(len(x_values)) if j != k])


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
