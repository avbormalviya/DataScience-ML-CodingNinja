
# Problem statement

"""
Given File 'amazonjobsdataset.csv'
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
"""

# Problem Statement :

"""
Find the month having most job openings in Year 2018 ?
Print the month (Month Name i.e January, February, March) and Number of job opening as Integer Value

Output Format :
MonthName Count
"""


# Solution


import csv

# Dictionary to store job counts per month in 2018
max_jobs_month_2018 = {}

# Opening the dataset file
with open("amazon_jobs_dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        # Extracting posting date
        posting_date = row.get("Posting_date", "").strip()

        # Splitting into Month and Year
        month, year = posting_date.split(",")

        # Extracting the month name
        month = month.split()[0].strip()

        # Counting only jobs posted in 2018
        if year.strip() == "2018":
            max_jobs_month_2018[month] = max_jobs_month_2018.get(month, 0) + 1


# Finding the month with the maximum job postings
month_name = max(max_jobs_month_2018, key=max_jobs_month_2018.get)
print(f"{month_name} {max_jobs_month_2018[month_name]}")
