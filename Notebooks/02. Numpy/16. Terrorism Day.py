# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
Find the number of attack held between day 10 and day 20?(ignoring the year and month)(including both day)

Print count of NumberOFAttack as integer value.

Output Format :
count
"""

# Solution

import csv
import numpy as np  # Importing NumPy

day = []  # List to store day values

# Reading dataset
with open("terrorism_dataset.csv", 'r', encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        value = row["Day"].strip()  # Removing extra spaces
        day.append(value if value else "0")  # Replace empty values with "0"

# Convert list to NumPy array and ensure integer conversion
day = np.array(day, dtype=int)

# Filtering days in the range 10 to 20
filtered_days = day[(day >= 10) & (day <= 20)]

# Print the count of days in this range
print(len(filtered_days))
