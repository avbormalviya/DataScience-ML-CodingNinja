
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during
this time period

Problem Statement :
Find top 5 Indian Cities which has most number of casualties ?

Print top 5 cities along with total casualties in that city. Print count of Casualty as integer value.

Note: Ignoring the City which is Unknown.

Casualty = Killed + Wounded.

Output Format :
city_1 casualty_1
city_2 casualty_2
city_3 casualty_3
city_4 casualty_4
city_5 casualty_5
"""


# Solution

import csv
import numpy as np
from collections import defaultdict, Counter

city_list = []
casualty_list = []

# Open the dataset file
with open("terrorism_dataset.csv", encoding="utf8") as file_obj:
    data = csv.DictReader(file_obj, skipinitialspace=True)

    # Filtering data for India and known cities
    for row in data:
        if row["Country"] == "India" and row["City"] != "Unknown":
            city_list.append(row["City"])
            casualty_list.append([row["Killed"], row["Wounded"]])

# Convert to NumPy arrays
np_city = np.array(city_list)
np_casualty = np.array(casualty_list, dtype=str)

# Replace empty values with "0.0" and convert to float
np_casualty[np_casualty == ""] = "0.0"
np_casualty = np.array(np_casualty, dtype=float)

# Calculate total casualties per incident
total_casualties = np.sum(np_casualty, axis=1)

# Dictionary to store total casualties per city
city_casualty_map = defaultdict(float)

# Efficiently aggregate casualties per city
for city, casualty in zip(np_city, total_casualties):
    city_casualty_map[city] += casualty

# Get the top 5 most affected cities
top_5_cities = Counter(city_casualty_map).most_common(5)

# Print results
for city, count in top_5_cities:
    print(city, int(count))
