from random import uniform

# Decimal digit precision
PRECISION = 10

def generate_x_values(n, value_range):
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