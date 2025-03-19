
# Problem statement

"""
Given a 2D list, create a numpy 2D array using it.

Note: Given 2D list is [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Print the Numpy array.

Output Format :
numpyArray
"""


# Solution


import numpy as np  # Importing the NumPy library

arr = [  # Defining a 2D list (nested list)
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numpyArray = np.array(arr)  # Converting the list into a NumPy array

print(numpyArray)  # Printing the NumPy array
