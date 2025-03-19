
# Problem statement

"""
Given file "terrorism_dataset.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have
occurred during this time period

Problem Statement :
Find value of killed column only where country == ‘United States’?

Print 0 in place of missing values.

Print count of Killed as integer value.

Output Format :
Killed1
Killed2
Killed3
Killed4
...
...
...
"""


# Solution

import csv
import numpy as np  # Importing NumPy library

# Lists to store the data
killed = []
country = []

# Reading the dataset
with open("terrorism_dataset.csv", 'r', encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        killed.append(row["Killed"])  # Collecting killed data
        country.append(row["Country"])  # Collecting country data

# Converting lists to NumPy arrays
killed = np.array(killed, dtype=str)  # Ensuring data is treated as strings initially
country = np.array(country, dtype=str)

# Replacing empty values with "0" before converting to numbers
killed[killed == ""] = "0.0"

# Convert killed values to integers (handling float values properly)
killed = np.array(killed, dtype=float).astype(int)

# Filtering records where the country is "United States"
indices = country == "United States"

# Displaying the number of people killed in the United States
print(*killed[indices], sep="\n")
