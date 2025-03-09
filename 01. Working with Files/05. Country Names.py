
# Problem Statement

""" Open and read the file

Print the country names from first 10 rows (in different lines)

Output Format :
Country 1
Country 2
Country 3
and so on """


# Solution

import csv  # Import the CSV module to handle CSV files

# Open the CSV file in read mode
with open("dataset.csv", "r") as fileObj:
    reader = csv.reader(fileObj)  # Create a CSV reader object

    next(reader)  # Skip the header row (if applicable)

    # Read and print the third column for the first 10 rows
    for _ in range(10):
        try:
            print(next(reader)[2])  # Print only the third column (index 2)
        except StopIteration:
            break  # Stop if the file has fewer than 10 rows
