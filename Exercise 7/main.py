from functions import least_squares_2, least_squares_3, least_squares_4


# Define main function
def main():
    # Closings for OPAP stock before 23/6/2023
    OPAP = [16.0800, 16.2500, 16.3900, 16.5800, 16.4400, 16.8400, 16.0000, 16.0000, 16.0500, 15.9000]

    # Calculate expected closing for 23/6/2023
    OPAP_ls2 = least_squares_2([10, 11, 12, 13, 14, 15], range(1, 11), OPAP)
    print(OPAP_ls2)

    OPAP_ls3 = least_squares_3([10, 11, 12, 13, 14, 15], range(1, 11), OPAP)
    print(OPAP_ls3)

    OPAP_ls4 = least_squares_4([10, 11, 12, 13, 14, 15], range(1, 11), OPAP)
    print(OPAP_ls4)


# Call main function
if __name__ == "__main__":
    main()