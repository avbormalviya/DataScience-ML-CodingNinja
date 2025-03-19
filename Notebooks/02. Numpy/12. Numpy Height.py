# Problem statement

"""
Given age and height of 20 students in two different numpy arrays with name age and height (in cms).
Print the age of those students whose height is above 155 cm.

Print the Numpy array.

Output Format :
age1 height1
age2 height2
...
"""

# Solution

import numpy as np  # Importing NumPy library

# Age and height arrays
age = np.array([15, 17, 19, 20, 14, 21, 16, 19, 13, 20, 22, 23, 21, 16, 18, 19, 20, 15, 17, 18])
height = np.array([156, 144, 180, 162, 152, 157, 154, 155, 151, 150, 158, 179, 126, 182, 183, 154, 159, 160, 172, 149])

# Finding indices where height is greater than 155
indices = height > 155  # Using boolean mask instead of np.where()

# Printing age and height values that match the condition
print("\n".join(f"{a} {h}" for a, h in zip(age[indices], height[indices])))
