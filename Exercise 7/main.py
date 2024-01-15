from functions import *


# Define main function
def main():
    # Closings for OPAP stock before 23/6/2023
    OPAP = [16.0800, 16.2500, 16.3900, 16.5800, 16.4400, 16.8400, 16.0000, 16.0000, 16.0500, 15.9000]

    # Calculate expected closing for 23/6/2023
    OPAP_ls2 = least_squares_2([10, 11, 12, 13, 14, 15], range(1, 11), OPAP)
    OPAP_ls3 = least_squares_3([10, 11, 12, 13, 14, 15], range(1, 11), OPAP)
    OPAP_ls4 = least_squares_4([10, 11, 12, 13, 14, 15], range(1, 11), OPAP)
    
    # Print results
    print("OPAP stock closings before 23/6/2023")
    print("Results calculated by the least squares methods:")
    print(f"Second degree polynomial:\n\tNext day: {OPAP_ls2[0]}\n\tNext five days: {OPAP_ls2[1::]}")
    print(f"Third degree polynomial:\n\tNext day: {OPAP_ls3[0]}\n\tNext five days: {OPAP_ls3[1::]}")
    print(f"Fourth degree polynomial:\n\tNext day: {OPAP_ls4[0]}\n\tNext five days: {OPAP_ls4[1::]}")

    # Closings for DEH stock before 23/6/2023
    DEH = [10.1500, 10.2200, 10.2500, 10.1700, 10.1000, 10.1800, 10.1200, 10.1000, 10.1000, 9.9850]

    # Calculate expected closing for 23/6/2023
    DEH_ls2 = least_squares_2([10, 11, 12, 13, 14, 15], range(1, 11), DEH)
    DEH_ls3 = least_squares_3([10, 11, 12, 13, 14, 15], range(1, 11), DEH)
    DEH_ls4 = least_squares_4([10, 11, 12, 13, 14, 15], range(1, 11), DEH)

    # Print results
    print("\nDEH stock closings before 23/6/2023")
    print("Results calculated by the least squares methods:")
    print(f"Second degree polynomial:\n\tNext day: {DEH_ls2[0]}\n\tNext five days: {DEH_ls2[1::]}")
    print(f"Third degree polynomial:\n\tNext day: {DEH_ls3[0]}\n\tNext five days: {DEH_ls3[1::]}")
    print(f"Fourth degree polynomial:\n\tNext day: {DEH_ls4[0]}\n\tNext five days: {DEH_ls4[1::]}")
    

# Call main function
if __name__ == "__main__":
    main()
