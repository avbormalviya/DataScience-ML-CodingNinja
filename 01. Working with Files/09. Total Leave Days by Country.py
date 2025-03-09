
# Problem Statement

""" Find the total number of leave days taken in each country.

Print the country name and the total leave days taken as an integer value.

Output Format:
Country_1 Total_Leave_1
Country_2 Total_Leave_2
Country_3 Total_Leave_3
... """


# Solution


import csv

# Dictionary to store country-wise leave days
country_leave_days = {}

# Open and read the dataset
with open("dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        country = row["Country"].strip().lower() if row["Country"] else "Unknown"
        leave_days = int(row["Leave_Days"].strip()) if row["Leave_Days"] and row["Leave_Days"].strip() else 0

        # Add leave days to the respective country
        country_leave_days[country] = country_leave_days.get(country, 0) + leave_days

# Print the result
for country, leave_days in country_leave_days.items():
    print(f"{country.capitalize()} {leave_days}")
