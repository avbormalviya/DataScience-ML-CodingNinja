
# Problem statement

"""
Given File - amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
"""

# Problem Statement :

""" 
What are the total number of job openings related to Computer Vision ?

Note:For finding the job related to computer vision check the Job Title column.
Print the count as the Integer Value

Output Format :
Count
"""


# Solution

import csv

# Initializing a counter for job titles containing "computer"
count_computer_vision = 0

# Opening the dataset file
with open("amazon_jobs_dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)

    for row in reader:
        # Safely extracting the job title to avoid errors if the column is missing
        title = row.get("Title", "").strip().lower()

        # Checking if the word "computer" appears in the title
        if "computer" in title:
            count_computer_vision += 1

# Printing the final count of matching job titles
print(count_computer_vision)
