
# Problem statement

"""
Find and print the minimum, maximum and average value of the feature for each kind of flower ?

Note: Get the dataset from here
Print the value with two decimal places.
Note: Order for flower is Iris-setosa, Iris-versicolor and Iris-virginica.

Output Format
minSL minSW minPL minPW Iris-setosa
maxSL maxSW maxPL maxPW Iris-setosa
avgSL avgSW avgPL avgPW Iris-setosa
...
...
...
"""


# Solution


import pandas as pd

# Define column names and load dataset
columns = ['sl', 'sw', 'pl', 'pw', 'flower_type']
iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names=columns)


# Function to print min, max, and mean values for each flower type
def print_flower_stats(flower_name):
    df = iris[iris.flower_type == flower_name]

    min_values = df.min(numeric_only=True)
    max_values = df.max(numeric_only=True)
    mean_values = df.mean(numeric_only=True)

    print(f"{min_values['sl']:.2f} {min_values['sw']:.2f} {min_values['pl']:.2f} {min_values['pw']:.2f} {flower_name}")
    print(f"{max_values['sl']:.2f} {max_values['sw']:.2f} {max_values['pl']:.2f} {max_values['pw']:.2f} {flower_name}")
    print(f"{mean_values['sl']:.2f} {mean_values['sw']:.2f} {mean_values['pl']:.2f} {mean_values['pw']:.2f} {flower_name}")


# Process all flower types
for flower in iris["flower_type"].unique():
    print_flower_stats(flower)
