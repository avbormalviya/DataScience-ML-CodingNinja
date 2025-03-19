
# Problem statement

"""
Sort a given 2D array of shape (4, 5) by 2nd column (i.e. column at index 1) in ascending order.

That means, we should re-arrange complete row based on 2nd columns' values.

Given 2D array is:

 [[21 20 19 18 17]
  [16 15 14 13 12]
  [11 10  9  8  7]
  [ 6  5  4  3  2]]
Print the 2D array in sorted order.

Note you have to generate the 2D Array.Here 2nd column means column present at index 1.

Output Format :
[[ 6  5  4  3  2]
[11 10  9  8  7]
[16 15 14 13 12]
[21 20 19 18 17]]
"""


# Solution

import numpy as np  # Importing NumPy library

# Creating a 4x5 array with numbers from 21 to 2 in descending order
arr = np.arange(21, 1, -1).reshape(4, 5)

# Sorting the array based on the values in the second column
arr = arr[arr[:, 1].argsort()]

# Displaying the sorted array
print(arr)
