# Problem statement

"""
Your task is to find the point of inclination by visualizing the plot for the given points on the x and y-axis.

You need to follow these steps:

1. Create two arrays, x and y.
2. x should hold the first 20 even points starting from 0 and y should be an exponentiation array where
                          y[i] = 2^x[I].
3. Plot a line graph, the line should be of the color blue and it should be a dashed line (like -----).
4. Find the value of x from where there is a slight increase in the value of y as shown in your plot.
Expected Output

Plot and print the value of x.

**Note**: Printed x must be a multiple of 5.
Output Format
x
"""

# Solution


import numpy as np
import matplotlib.pyplot as plt

# Generate x values (even numbers from 0 to 38)
x = np.arange(0, 40, 2)

# Compute y values as an exponential function
y = 2 ** x

# Plot with dashed line and markers
plt.plot(x, y, '--o', color='blue', label="y = 2^x")

# Add labels and title
plt.xlabel("X values")
plt.ylabel("Y values (log scale)")
plt.title("Exponential Growth of 2^x")

# Enable grid and legend
plt.grid(True)
plt.legend()

# Show plot
plt.show()

# Clarified print statement
print(30)
