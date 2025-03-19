
# Problem statement

"""
You are given a rope of length 5m. Cut the rope into 9 parts such that each part is of equal length.

Note:Array elements are the points where cut is to be made and round upto 2 decimal place.

Print the array element.

Output Format :
element1
element2
element3
.
.
"""


# Solution

import numpy as np

length = 5  # Total length of the rope
parts = 9  # Number of parts

# Generate 8 evenly spaced cut positions (excluding 0 and 5)
cut_positions = np.round(np.linspace(length / parts, length - length / parts, parts - 1), 2)

# Print the cut positions
print(cut_positions)
