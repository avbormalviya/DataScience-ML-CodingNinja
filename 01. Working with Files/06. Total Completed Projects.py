
# Problem Statement

""" Find and print the total number of completed projects.

Print the count as an integer value.

Note: There can be missing values in the "Projects_Completed" column. You should try to print the values of
the "Projects_Completed" column and observe.

Output Format:
Count """


# Solution


import csv  # Import CSV module to handle CSV files

# Open CSV file in read mode
with open("dataset.csv", "r") as fileObj:
    reader = csv.reader(fileObj, skipinitialspace=True)  # Removes leading spaces

    next(reader)  # Skip header row

    total_sum = 0  # Initialize sum

    for row in reader:
        if len(row) > 6 and row[6].strip():  # Ensure row has at least 7 columns & column isn't empty
            try:
                total_sum += float(row[6])  # Convert to float and add to sum
            except ValueError:  # Skip rows with non-numeric values in column 6
                continue

    print(int(total_sum))  # Print the total as an integer
