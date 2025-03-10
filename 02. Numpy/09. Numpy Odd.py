
# Problem statement

"""
Given an integer array of size 10. Replace the odd number in numpy array with -1 ?

Note: Generate the following array

array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Print the Numpy array.

Output Format :
firstElement secondElement  ...
"""


# Solution

import numpy as np  # Importing the NumPy library

arr = np.arange(1, 11)  # Create a NumPy array [1, 2, 3, ..., 10]

indices = arr % 2 != 0  # Find indices where elements are odd

arr[indices] = -1  # Replace all odd elements with -1

print(arr)  # Print the modified array
