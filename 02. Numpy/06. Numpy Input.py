
# Problem statement

"""
Given a 2D integer array size (4, 5) with name input_?

Print elements of highlighted matrixes

[[1, 2, 3, 4, 5],
 [6, 7, 8, 9, 10],
 [>11<, >12<, >13<, 14, 15],
 [16, 17, 18, 19, 20]]

[[1, 2, 3, 4, 5],
 [6, 7, 8, >9<, 10],
 [11, 12, 13, >14<, 15],
 [16, 17, 18, >19<, 20]]

[[1, 2, 3, 4, 5],
 [6, 7, 8, 9, 10],
 [>11<, >12<, >13<, >14<, >15<],
 [>16<, >17<, >18<, >19<, >20<]]

[[1, 2, 3, 4, 5],
 [6, >7<, >8<, 9, 10],
 [11, >12<, >13<, 14, 15],
 [16, 17, 18, 19, 20]]


Output Format :
element1 element2 element3 ...
element1 element2 element3 ...
element1 element2 element3 ...
element1 element2 element3 ...
"""


# Solution

import numpy as np  # Importing the NumPy library

# Creating a 2D NumPy array (4x5 matrix)
arr = np.array([[1,  2,  3,  4,  5],
                [6,  7,  8,  9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])

# Selecting elements from the 3rd row (index 2), from columns 0 to 2 (inclusive of 0, exclusive of 3)
print(arr[2, 0:3])

# Selecting elements from rows 2 to 4 (index 1 to 3) and column 3 (fourth column)
print(arr[1:4, 3])

# Selecting elements from rows 3 to 4 (index 2 to 3) and all columns (0 to 4)
print(arr[2:4, :5])

# Selecting a submatrix from rows 2 to 3 (index 1 to 2) and columns 2 to 3 (index 1 to 2)
print(arr[1:3, 1:3])
