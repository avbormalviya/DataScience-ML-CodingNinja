
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have
occurred during this time period

Problem Statement :
Find out the Country with Highest Number of Terror Attack and in which year the most number of terrorist
attack happened in that country ?

Print count of terror attacks as integer value.

Output Format :
Country NumberOfAttack Year
"""


# Solution


import pandas as pd

# Load the dataset
df = pd.read_csv("terrorism_dataset.csv")

# Get the country with the most incidents
top_country = df['Country'].mode()[0]
df = df[df['Country'] == top_country]

# Get the total number of incidents in that country
total_attacks = df.shape[0]

# Find the year with the most incidents
year_counts = df['Year'].value_counts()
most_active_year = year_counts.idxmax()

# Print results
print(top_country, total_attacks, most_active_year)
