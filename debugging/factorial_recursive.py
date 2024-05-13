#!/usr/bin/python3
import sys

def factorial(n):
    """
	Calculate the factorial of a given number.

	Args:
	    n (int): The number for which factorial needs to be calculated.

	Returns:
	    int: The factorial of the given number.
     """

	 if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the number from the command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the factorial
print(f)
