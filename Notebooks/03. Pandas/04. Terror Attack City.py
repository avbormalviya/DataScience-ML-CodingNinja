
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that
have occurred during this time period

Problem Statement :
The Most Dangerous city in Jammu and Kashmir and the terrorist group which is most active in that city?
Print count of number of attacks in that city as integer value.

Note:Ignoring the Unknown Terrorist Group.Here Dangerous related with the number of terrorist attacks.

Output Format :
City NumberOfAttack Group
"""


# Solution


import pandas as pd

# Load dataset
data = pd.read_csv('terrorism_dataset.csv')

# Filter for Jammu and Kashmir
data = data[data['State'] == 'Jammu and Kashmir']

# Get the most attacked city
city_list = data['City'].value_counts()

city = city_list.index[0]  # City with the most attacks

attack = city_list.values[0]  # Number of attacks

# Filter for that city
data = data[data['City'] == city]

# Get the most active terror group (excluding 'Unknown' if present)
group_counts = data['Group'].value_counts()
if 'Unknown' in group_counts.index:
    group_counts = group_counts.drop('Unknown')

# Handle cases where all groups are 'Unknown'
group = group_counts.index[0] if not group_counts.empty else 'Unknown'

# Output result
print(city, attack, group)
