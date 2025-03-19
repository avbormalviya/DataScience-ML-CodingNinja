
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during
this time period

Problem Statement :
Find the most frequent day of attack in a terrorismDataset ?

Note: Here np.unique can be used.

Print count of frequent day and number of attack as Integer value.

Output Format :
Day NumberOFAttack
"""


# Solution

import csv
import numpy as np

# Read 'Day' values from dataset
with open("terrorism_dataset.csv", encoding="utf8") as file_obj:
    data = csv.DictReader(file_obj, skipinitialspace=True)

    day = np.array([row.get("Day", "").strip() for row in data])

# Replace empty strings with "0" to avoid conversion issues
day[day == ""] = "0"

# Convert to integers
day = day.astype(int)

# Get unique values & their counts
values, counts = np.unique(day, return_counts=True)

# Find the most frequent day
most_frequent_day = values[np.argmax(counts)]

# Print result
print(most_frequent_day, counts.max())
