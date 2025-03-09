
# Problem statement

"""
Given File 'amazonjobsdataset.csv'
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
"""

# Problem Statement :

"""
Find the country does Amazon need the most number of Java Developer?
Print the Country(Country Shortcut as given in Dataset) and number of job opening as integer value

Note :Here we will use the BASIC QUALIFICATIONS feature to find out whether Java is required for the job or not.
Keyword is used is 'Java'.(Here case should not be changed).

Output Format :
Country NumberofJobs For example : US 40
"""


# Solution


import csv  # Import CSV module

country_count = {}  # Dictionary to store Java job count per country

# Open the dataset file safely
with open("amazon_jobs_dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)  # Read CSV file as dictionary

    for row in reader:
        # Safely get the 'BASIC QUALIFICATIONS' and 'location' columns
        qualifications = row.get("BASIC QUALIFICATIONS", "").strip()
        location = row.get("location", "").strip()

        # Check if "Java" is in qualifications (case insensitive)
        if "Java" in qualifications:
            country = location.split(",")[0].strip().lower()  # Extract the country name

            # Use .get() for cleaner dictionary update
            country_count[country] = country_count.get(country, 0) + 1

# Find the country with the most Java-related jobs
max_country = max(country_count, key=country_count.get)
print(max_country, country_count[max_country])
