
# Problem statement

""" Open and read the file

Print the first 3 rows of the file, excluding header (in different lines)

Print columns of one row, separated by space

Output Format :
col_1 col_2 col_3 col_4 ....
col_1 col_2 col_3 col_4 ....
col_1 col_2 col_3 col_4 .... """


# Solution


import csv  # Import the CSV module to handle CSV file operations

# Open the CSV file in read mode
with open("dataset.csv", "r") as fileObj:
    reader = csv.reader(fileObj)  # Create a CSV reader object

    # Read and print the first 3 rows using `next()`
    for _ in range(3):
        print(*next(reader))  # `*` unpacks the row for cleaner output
