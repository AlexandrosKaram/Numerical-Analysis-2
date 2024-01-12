import numpy as np
from random import uniform

RANGE = (0, 2*np.pi)

def main():
    # Generate 10 random numbers between 0 and 2pi
    x_values = [round(uniform(*RANGE), 5) for i in range(10)]
    x_values.sort()
    # Calculate the sine of each value
    y_values = [round(np.sin(x), 5) for x in x_values]
    

main()