
# Problem Statement

""" Find and print the total number of projects completed by people who are from the country "India".
Print the count as an integer value.

Note: There can be missing values in the "Projects_Completed" column. You should try to print the values of the "Projects_Completed" column and observe.

Output Format:
Count """


# Solution


import csv

# Open CSV file in read mode
with open("dataset.csv", "r") as fileObj:
    reader = csv.reader(fileObj, skipinitialspace=True)  # Remove leading spaces

    next(reader)  # Skip header row

    total_sum = 0  # Initialize sum

    for row in reader:
        # Ensure row has at least 7 columns & row[6] isn't empty
        if len(row) > 6 and row[6].strip() and row[2].strip().lower() == "india":
            try:
                total_sum += int(row[6])  # Convert to integer and add
            except ValueError:
                continue  # Skip rows where row[6] isn't a valid integer

    print(total_sum)  # Print the total sum
