
# Problem statement

"""
In a given 1D array, convert all elements that fall between 3 and 8 (both inclusive) to negative numbers.

Note: Generate the following array

array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Print the Numpy array.

Output Format :
firstElement
secondElement
...
"""


# Solution

import numpy as np  # Importing NumPy library

arr = np.arange(1, 11)  # Creating an array from 1 to 10

arr[3:9] *= -1  # Directly negating elements from index 3 to 8

print(arr)  # Printing the modified array
