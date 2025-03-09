
# Problem statement

"""
Given File 'amazon_jobs_dataset.csv'
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
"""

# Problem Statement :

"""
Find the number of job openings are present if applicant have Bachelor degree?
Print the count as Integer value

Note : Here we will use the BASIC QUALIFICATIONS feature to find out whether bachelor degree for Job is required or not.
Keywords that can be used are 'Bachelor', 'BS' and 'BA'. 

Output Format :
Count 
"""


# Solution


import csv  # Importing the CSV module to handle file operations

count = 0  # Variable to keep track of the count of jobs requiring a Bachelor's degree

# Opening the dataset file in read mode
with open("amazon_jobs_dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)  # Reading the CSV file as a dictionary

    for row in reader:
        # Extract the 'BASIC QUALIFICATIONS' column and remove unnecessary spaces
        basic_qualifications = row.get("BASIC QUALIFICATIONS", "").strip()

        # Check if any variation of a Bachelor's degree is mentioned
        if "Bachelor" in basic_qualifications or "BS" in basic_qualifications or "BA" in basic_qualifications:
            count += 1  # Increment count if a match is found

# Print the final count of job postings requiring a Bachelor's degree
print(count)
