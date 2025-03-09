
# Problem statement

""" Given File 'amazonjobsdataset.csv'
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
"""

# Problem Statement :

""" Find the number of job openings in Canada?
Print the count as the Integer Value
Note: Here you should analyse the country code in location feature.( you can use dictionary for analyse part ). 

Output Format :
Count
"""


# Solution


import csv

# Counter for job listings in Canada
count_canada = 0

# Opening the dataset file
with open("amazon_jobs_dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        # Safely extracting location to avoid errors
        location = row.get("location", "").strip().lower()

        # Splitting location into parts based on commas
        location_parts = [part.strip() for part in location.split(",")]

        # Checking if 'ca' appears at the first position (indicating Canada)
        if location_parts and location_parts[0] == "ca":
            count_canada += 1

# Printing the final count of job listings in Canada
print(count_canada)
