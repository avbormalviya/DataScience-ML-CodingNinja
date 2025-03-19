
# Problem statement

"""
Given an integer array of size 9 and replace the first occurrence of maximum value by 0?

Note: Generate the following array

array([11, 2, 13, 4, 15, 6, 27, 8, 19])
Print the Numpy array.

Output Format :
firstElement
secondElement
...
"""


# Solution

import numpy as np  # Importing the NumPy library

arr = np.array([11, 2, 13, 4, 15, 6, 27, 8, 19])  # Creating a NumPy array

max_value_index = arr.argmax()  # Finding the index of the maximum value

arr[max_value_index] = 0  # Replacing the maximum value with 0

print(arr)  # Printing the modified array
