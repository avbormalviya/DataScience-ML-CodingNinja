
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that
have occurred during this time period

Problem Statement :
Most Deadliest attack in a history of HumanKind?

Print count of Killed people as integer value.

Note: Here Deadliest attack means, in which the most number of people killed.

Output Format :
NumberOfPeopleKilled Country TerroristGroup
"""


# Solution


import pandas as pd

# Load dataset
df = pd.read_csv("terrorism_dataset.csv")

# Convert 'Killed' column to numeric, replacing NaN with 0
df["Killed"] = pd.to_numeric(df["Killed"], errors="coerce").fillna(0)

# Get max killed value
max_killed = df["Killed"].max()

# Filter rows where 'Killed' is maximum
df_max = df[df["Killed"] == max_killed]

# Print all cases with max killed
for _, row in df_max.iterrows():
    print(int(row["Killed"]), row["Country"], row["Group"])
