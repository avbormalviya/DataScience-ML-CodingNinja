
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that have
occurred during this time period

Problem Statement :
There was formation of new government in India on 26 May 2014. So current government's span is from 26th May 2014
to current. Find out two things from this period-

1. Total number of attacks done in this period in India. Find this count as integer.
2. Which Terrorist group was most active in this period in India. Most active means, group which has done
maximum number of attacks.
3.Ignore the Unknown group.

Output Format :
TotalAttacks MostActiveTerroristGroup
"""


# Solution


import pandas as pd

# Load dataset
path = 'terrorism_dataset.csv'
df_terrorism = pd.read_csv(path, encoding='ISO-8859-1')

# Filter for attacks in India
df_terrorism = df_terrorism[df_terrorism['Country'] == 'India']

# Filter for attacks from May 26, 2014, onwards
df_terrorism = df_terrorism[(df_terrorism['Year'] > 2014) |
                            ((df_terrorism['Year'] == 2014) &
                             ((df_terrorism['Month'] > 5) |
                              ((df_terrorism['Month'] == 5) & (df_terrorism['Day'] >= 26))))]

# Count number of attacks
attack = df_terrorism.shape[0]

# Get most active terror groups (excluding 'Unknown')
group_counts = df_terrorism['Group'].value_counts()
if 'Unknown' in group_counts.index:
    group_counts = group_counts.drop('Unknown')

# Safely get the second most active group (if available)
group = group_counts.index[1] if len(group_counts) > 1 else 'Unknown'

# Print results
print(attack, group)
