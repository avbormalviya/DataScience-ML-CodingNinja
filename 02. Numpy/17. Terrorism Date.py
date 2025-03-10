
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during
this time period

Problem Statement :
Find the number of attack held between 1 Jan 2010 and 31 Jan 2010?(including both date).

Note Ignore the case where day is 0

Print count of NumberOFAttack as integer value.

Output Format :
count
"""


# Solution

import csv
import numpy as np  # Importing NumPy

date = []

# Reading dataset
with open("terrorism_dataset.csv", 'r', encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        # Handling missing values: replace empty fields with "0"
        day = row["Day"].strip() if row["Day"].strip() else "0"
        month = row["Month"].strip() if row["Month"].strip() else "0"
        year = row["Year"].strip() if row["Year"].strip() else "0"
        date.append([day, month, year])

# Convert list to NumPy array and ensure numeric conversion
date = np.array(date, dtype=float)

# Filtering data: Year = 2010, Month = 1, Day >= 1
date = date[(date[:, 2] == 2010) & (date[:, 1] == 1) & (date[:, 0] >= 1)]

# Print the count of filtered records
print(len(date))


