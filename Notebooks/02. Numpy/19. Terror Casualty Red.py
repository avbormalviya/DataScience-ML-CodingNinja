
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during
this time period

Problem Statement :
Find the casualty in the Red Corridor States ? Mainly Red corridor states include Jharkhand, Odisha, Andhra Pradesh, and Chhattisgarh.

Note: Casualty=Killed +Wounded

Print count of Casualty as integer value.

Output Format :
Count
"""


# Solution

import csv
import numpy as np  # Importing NumPy

casualty = []

# States to filter
target_states = {"Jharkhand", "Odisha", "Andhra Pradesh", "Chhattisgarh"}

# Reading dataset
with open("terrorism_dataset.csv", 'r', encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        state = row.get("State", "").strip()

        if state in target_states:
            # Handle missing values: Replace empty "Killed" and "Wounded" with '0'
            killed = row.get("Killed", "").strip() or "0"
            wounded = row.get("Wounded", "").strip() or "0"

            casualty.append([killed, wounded])

# Convert casualty list to NumPy array
casualty = np.array(casualty, dtype=float).astype(int)  # Convert to int

# Compute total casualties (Killed + Wounded)
total_casualties = np.sum(casualty)

# Output result
print(total_casualties)
