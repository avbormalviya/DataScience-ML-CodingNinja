
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during
this time period

Problem Statement :
As we knew the Kargil ( in Jammu and Kashmir) War that took place between May 1999 and July 1999 (3 Months) ,
so there was a huge conflict in Kashmir Valley during this period.

In this dataset, there is no information regarding the war between the two countries to
find out the casualty during the war.

So find out the attack in this period in which maximum casualties happened.

Print the count of casualties (as integer), city in which that attack happened and name of attack group.

Note : Casualty = Killed + Wounded.Fill the empty value in killed or wounded feature to 0.

Output Format :
Casualty City TerroristGroup
"""


# Solution

import csv
import numpy as np  # Importing NumPy

city = []
casualty = []

# Reading dataset
with open("terrorism_dataset.csv", 'r', encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        if row.get("State", "").strip() == "Jammu and Kashmir" and row.get("Year", "").strip() == "1999":
            if row.get("Month", "").strip() in {"5", "6", "7"}:
                # Handle missing values: Replace empty "Killed" and "Wounded" with '0'
                killed = row.get("Killed", "").strip() or '0'
                wounded = row.get("Wounded", "").strip() or '0'

                # Store data
                casualty.append([killed, wounded])
                city.append([row.get("City", "").strip(), row.get("Group", "").strip()])

# Convert lists to NumPy arrays
city = np.array(city)
casualty = np.array(casualty, dtype=float)  # Convert to float for calculations

# Compute total casualties (Killed + Wounded)
casualty = np.sum(casualty, axis=1)

# Get index of the city with max casualties
max_index = np.argmax(casualty)

# Output result
print(int(casualty[max_index]), city[max_index][0], city[max_index][1])
