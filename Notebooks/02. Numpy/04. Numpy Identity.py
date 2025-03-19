
# Problem statement

"""
Create a matrix having diagonal elements as 1 and all other elements as 0 of size (5, 5).

Print the Numpy array.

Output Format :
numpyArray
"""


# Solution

import numpy as np  # Importing NumPy

arr = np.identity(5, dtype=int)  # Creates an identity matrix of size 5

print(arr)  # Prints the array
