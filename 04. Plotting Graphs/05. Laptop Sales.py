# Problem statement

"""
Given data is having distribution of sales of different laptops for the year 2018 in India
(it has company name and number of laptops sold).

Plot a pie graph to show the %age distribution for the year 2018 and also print the value of
%age distribution of individual companies.

Note: Output should have company name and %age distribution (%age value should be upto 1 decimal place
without the % sign) , it should be in the same order as it is given.

Output Format:
company_name1 percentage1
company_name2 percentage2
...
...
...
"""

# Solution


import matplotlib.pyplot as plt
import numpy as np

# Given data
company = np.array(['HP', 'Dell', 'Lenovo', 'Asus', 'Apple', 'Acer'])
sold = np.array([20000, 43000, 15000, 17000, 22000, 13000])

# Pie chart with enhancements
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']  # Custom colors
explode = (0, 0.1, 0, 0, 0, 0)  # Highlighting Dell

plt.figure(figsize=(8, 6))
plt.pie(sold, labels=company, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode,
        shadow=True, textprops={'fontsize': 12}, wedgeprops={'edgecolor': 'black'})

plt.title("Market Share of Laptop Brands", fontsize=14)
plt.show()

# Calculate and print percentage share manually
sold_percentage = np.true_divide(sold, sold.sum(axis=0, keepdims=True)) * 100

for i in range(len(sold)):
    print(f"{company[i]}: {sold_percentage[i]:.1f}%")
