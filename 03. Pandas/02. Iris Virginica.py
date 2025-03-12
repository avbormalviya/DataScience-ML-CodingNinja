
# Problem statement

"""
Find the data of flower “Iris-virginica” type where petal-length > 1.5?

Note: Get the dataset from here

Hint:
1. You first filter the dataset to include only the species 'Iris-virginica'.
2. Then, you further filter the dataset by keeping rows where PetalLength is greater than 1.5.
3. Finally, the loop goes through each row and column, printing each value in the filtered data set.

Print the all the feature values.
"""


# Solution


import pandas as pd

# Load the dataset
url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
iris = pd.read_csv(url)

# Filter rows where variety is 'Virginica' and petal length is greater than 1.5
filtered_df = iris.query("variety == 'Virginica' and `petal.length` > 1.5")

# Display the result
print(filtered_df)
