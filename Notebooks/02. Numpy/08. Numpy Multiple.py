
# Problem statement

"""
Given an integer array of size 10. Print the index of elements which are multiple of 3.

Note: Generate the following array

array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])
Print the index of elements.

Output Format :
index1 index2 index3 ...
"""


# Solution

import numpy as np  # Importing the NumPy library

arr = np.arange(1, 20, 2)  # Create an array of odd numbers from 1 to 19

indices = np.where(arr % 3 == 0)  # Find indices where elements are divisible by 3

print(*indices)  # Print indices without tuple formatting
