
# Problem statement

"""
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017.
This dataset includes systematic data on domestic as well as international terrorist incidents that
have occurred during this time period

Problem Statement :
Find the frequency of the Casualty in Red Corridor states and in Jammu and Kashmir ?Here Frequency is
(Total Casualty/Total Number of a year)

Print frequency as integer value.

Note:Red Corridor state includes Jharkhand, Odisha, Andhra Pradesh, and Chhattisgarh. Here Casualty=Killed +Wounded.
Don't fill the nan value present in Killed and Wounded feature.

Output Format :
Frequency1 Frequency2
"""


# Solution


import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('terrorism_dataset.csv')

# Filter only India data first
df = df[df['Country'] == 'India']

# Count unique years for India (ensuring accuracy)
year_count = df['Year'].nunique()

# Convert 'Killed' and 'Wounded' to numeric, handling NaN values
df['Killed'] = pd.to_numeric(df['Killed'], errors='coerce').fillna(0).astype(int)
df['Wounded'] = pd.to_numeric(df['Wounded'], errors='coerce').fillna(0).astype(int)

# Calculate total casualty
df['Casualty'] = df['Killed'] + df['Wounded']

# Filter Jammu & Kashmir data
jk = df[df['State'] == 'Jammu and Kashmir']

# Filter Red Corridor states
red_corridor_states = ["Jharkhand", "Odisha", "Andhra Pradesh", "Chhattisgarh"]
rc = df[df['State'].isin(red_corridor_states)]

# Compute total casualties
jkc = jk['Casualty'].sum()
rcc = rc['Casualty'].sum()

# Print average casualties per year
print(rcc // year_count, jkc // year_count)
