
# Problem Statement

""" Find the most hardworking employee in terms of Hours Worked.

If multiple employees have the same highest hours worked, print all their names.

For any missing value in the Hours_Worked column, take it as 0.

Output Format:
Employee_1 Hours_Worked
Employee_2 Hours_Worked
Employee_3 Hours_Worked
... """


# Solution


import csv

# Variables to track the highest hours worked and corresponding employees
max_hours = 0
hardworking_employees = []

# Open and read the dataset
with open("dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        # Handle missing or empty Hours_Worked values
        hours_worked = int(row["Hours_Worked"].strip()) if row["Hours_Worked"] and row["Hours_Worked"].strip() else 0

        # Get employee name
        name = row["Name"].strip() if row["Name"] else "Unknown"

        # Update max hours and employee list
        if hours_worked > max_hours:
            max_hours = hours_worked
            hardworking_employees = [(name, hours_worked)]  # Reset list with new max
        elif hours_worked == max_hours:
            hardworking_employees.append((name, hours_worked))  # Add to list if tie

# Print results
for name, hours in hardworking_employees:
    print(f"{name} {hours}")
