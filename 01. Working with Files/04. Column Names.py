
# Problem Statement

""" Open and read the file

Print the name of columns (in different lines)

Output Format :
Column 1
Column 2
Column 3
and so on """


# Solution


import csv  # Import the CSV module to handle CSV files

# Open the CSV file in read mode
with open("dataset.csv", "r") as fileObj:
    reader = csv.reader(fileObj)  # Create a CSV reader object

    headers = next(reader)  # Read the first row (column names)

    # Print each column name on a new line
    for column in headers:
        print(column.strip())
