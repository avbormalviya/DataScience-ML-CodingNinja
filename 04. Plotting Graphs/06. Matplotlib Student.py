# Problem statement

"""
Given height (in centimetre) and weight (in kilograms) of 20 students, Plot a two different histogram of
height and weight. whereas divide the data in 5 bins.

From histogram, find the value of the height and weight in which the value of y-axis is maximum.
Print starting value of bin where y is maximum. For eg. if for height with range 50 to 55 is maximum,
then print 50. Print the value as integer (after rounding off). (to answer this please look closely to the graph)

Plot the histogram and print the value.

Output Format
height_value weight_value
"""

# Solution


import numpy as np
import matplotlib.pyplot as plt

# Given data
height = [189, 185, 195, 149, 189, 147, 154, 174, 169, 195, 159, 192, 155, 191, 153, 157, 140, 144, 172, 157]
weight = [87, 110, 104, 61, 104, 92, 111, 90, 103, 81, 80, 101, 51, 79, 107, 110, 129, 145, 139, 110]

# Plot histograms with improvements
plt.figure(figsize=(8, 6))
plt.hist(height, bins=5, alpha=0.6, color='blue', edgecolor='black', label='Height')
plt.hist(weight, bins=5, alpha=0.6, color='red', edgecolor='black', label='Weight')

# Labels and title
plt.xlabel("Value", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Distribution of Height & Weight", fontsize=14)

# Add legend
plt.legend()

# Show plot
plt.show()

# Print values
print(184, 89)
