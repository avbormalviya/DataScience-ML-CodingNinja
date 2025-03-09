
# Problem Statement

""" Find and print the total salary paid to people from the country "India".

Print the total as an integer value.

Note: There can be missing values in the "Salary" column and there may be some initial spaces present in every value. You should try to print the values of the "Salary" column and observe.

Output Format:
Total Salary """


# Solution


import csv

# Open CSV file in read mode
with open("dataset.csv", "r") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)  # Read as dictionary

    total_sum = 0  # Initialize sum

    for row in reader:
        if row["Country"].strip().lower() == "india" and row["Salary"].strip():
            try:
                total_sum += int(row["Salary"])  # Convert to integer and add
            except ValueError:
                continue  # Skip if Salary is non-numeric

    print(total_sum)  # Print the total sum
