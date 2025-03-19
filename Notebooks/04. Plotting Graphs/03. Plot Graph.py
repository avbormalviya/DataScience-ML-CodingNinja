# Problem statement

"""
Plot the two graphs on same plot.The graph between the two given integer array X and Y and the graph between
two integer array X and Y where X should hold 20 even points starting from 0 and y should be equal to X where
y[i] = 2 * x[i].Plot should have x label and y label and the legend to differentiate between the two graphs. Consider,

x1 =[0,1,2,3,4,5,6,7,9,10]
y1=[1,2,5,10,17,26,37,50,82,101]
and
x2=np.arange(0,40,2)
y2=2*x2

Find the value x (in the range of 10) of both the plots when the value of y is 60
For each plot print the output to new line.

Output Format
lower_limit to upper_limit
lower_limit to upper_limit
"""

# Solution


import numpy as np
import matplotlib.pyplot as plt

# Given data
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]
y1 = [1, 2, 5, 10, 17, 26, 37, 50, 82, 101]

x2 = np.arange(0, 40, 2)
y2 = 2 * x2

# Plot first graph with markers
plt.plot(x1, y1, 'o--', color='blue', label='Graph 1 (x1, y1)')

# Plot second graph with a solid line
plt.plot(x2, y2, '-r', label='Graph 2 (x2, y2)')

# Add labels, legend, and grid
plt.xlabel('x')
plt.ylabel('y')
plt.title("Comparison of Two Graphs")
plt.legend()
plt.grid(True)

# Highlighting specific ranges
plt.axvspan(0, 10, color='yellow', alpha=0.2, label='0 to 10 range')
plt.axvspan(25, 35, color='green', alpha=0.2, label='25 to 35 range')

# Show plot
plt.show()

# Print statements clarification
print("Highlighted regions: 0 to 10 and 25 to 35.")
