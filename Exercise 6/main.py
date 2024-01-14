import numpy as np
# Import from parent directory
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from global_functions import generate_x_values
from functions import trapezoidal_integration, simpson_integration

# Range of values to generate [0, π/2]
RANGE = (0, np.pi/2)


# Define main function
def main():
    print("Integral of sin(x) from 0 to π/2:")
    print(f"Trapezoidal integration: {trapezoidal_integration(RANGE)}")


# Call main function
main()
