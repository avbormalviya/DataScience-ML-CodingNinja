
# Problem statement

""" Given File amazon_jobs_dataset.csv (Please check Dataset preview name)

It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site. """

# Problem Statement

""" Find number of job openings in Bangalore,IN and in Seattle,US?

Print the Number of Job opening in Bangalore and Seattle as Integer value.

Output Format :
CountBangalore CountSeattle """


# Solution


import csv

# Initializing counters for job listings in Bangalore and Seattle
count_bangalore = 0
count_seattle = 0

# Opening the dataset file
with open("amazon_jobs_dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        # Extracting location details safely to avoid errors if the key is missing
        location = row.get("location", "").strip().lower()

        # Splitting location into parts to handle different formats
        location_parts = [part.strip() for part in location.split(",")]

        # Checking if the job is listed in Bangalore
        if "bangalore" in location_parts:
            count_bangalore += 1

        # Checking if the job is listed in Seattle
        if "seattle" in location_parts:
            count_seattle += 1

# Printing the final counts for both locations
print(count_bangalore, count_seattle)
