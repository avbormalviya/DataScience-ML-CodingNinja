
# Problem statement

"""
Problem Statemnt:
Find indices of non-zero elements from the array [1,2,0,0,4,0] ?

Print the index of non-zero elements.

Output Format :
index1 index2 index3 ...
"""


# Solution

import numpy as np  # Importing the NumPy library

list = [1, 2, 0, 0, 4, 0]  # A Python list with some zero and non-zero elements

arr = np.array(list)  # Convert the list into a NumPy array

indices = np.where(arr != 0)  # Find indices where elements are NOT zero

print(*indices)  # Print the result
