
# Problem statement

"""
Find and print count of each kind of flower (separated by space)?

Note: Get the dataset from here
Print the count as Integer Value.

Output Format
count1 count2 count3 .....
"""


# Solution


import pandas as pd

# Load the dataset
url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
iris = pd.read_csv(url)

# Count occurrences of each variety
variety_counts = iris["variety"].value_counts()

# Print counts as space-separated values
print(*variety_counts.tolist())
