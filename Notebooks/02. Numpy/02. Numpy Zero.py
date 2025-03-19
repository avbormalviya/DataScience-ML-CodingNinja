
# Problem statement

"""
Create an integer array of size 10, where all the values should be 0 but the fifth value should be 1.

Print the elements of array.

Output Format :
element1 element2 element3 ...
"""


# Solution

import numpy as np  # Importing NumPy

arr = np.zeros(10, dtype=int)  # Creating an array of 10 zeros (integer type)

arr[4] = 1  # Setting the 5th element (index 4) to 1

print(arr)  # Printing the modified array
