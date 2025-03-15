# Problem statement

"""
We are given data of Microsoft Corporations, it contains the gross annual revenue in
billion U.S dollar and the number of employees in thousands and year. Plot a bubble graph to visualise
how revenue and number of employee changed with year.

Find years where there is a drastic increase in gross revenue of Microsoft Corporations (from previous and
next year both). Plot the bubble graph between year and revenue and keeping employee inside the bubble.
Print the year, revenue and number of the employee where there is a drastic increase in revenue ( Top 2 ).

Note:For finding the year where there is a drastic increase in gross revenue check whether the revenue of
that year is greater than in previous years and greater than next year. Here years should be printed in ascending order.

Output Format:
year1 revenue1 employee1
year2 revenue2 employee2
...
...
...
"""

# Solution


import matplotlib.pyplot as plt
import numpy as np

# Given data
employees = np.array([61,71,79,91,93,89,90,94,99,128,118,114,124,131])
year = np.array([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
revenue = np.array([39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36])

count = np.arange(len(year))

# Scatter plot
plt.figure(figsize=(10, 6))
sc = plt.scatter(year, revenue, c=count, s=employees * 5, alpha=0.9, edgecolor='black', marker='o', linewidths=1.2, cmap='viridis')

# Adding text labels to points
for i in range(len(year)):
    plt.text(year[i] + 0.2, revenue[i] + 0.5, employees[i], fontsize=10, ha='center')

# Add labels, title, grid, and colorbar
plt.xlabel("Year")
plt.ylabel("Revenue (in billion $)")
plt.title("Company Revenue and Employees Over Years")
plt.colorbar(sc, label="Index in Data")  # Colorbar for clarity
plt.grid(True, linestyle="--", alpha=0.5)

# Show plot
plt.show()

# Finding and printing data for specific years
for y in [2008, 2015]:
    idx = np.where(year == y)[0][0]
    print(f"Year: {year[idx]}, Revenue: {revenue[idx]}, Employees: {employees[idx]}")
