
# Problem statement

"""
Given File 'amazonjobsdataset.csv'
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
"""

# Problem Statement

"""
Among Java, C++ and Python, which of the language has more job openings in India for Bachelor Degree Holder?
Print the Language(i.e Java,C++,Python) and number of job opening as integer value.

Note : Here we will use the BASIC QUALIFICATIONS feature to find out whether bachelor degree for Job is required or not.
Keywords that can be used are 'Bachelor', 'BS' and 'BA' and we will use the BASIC QUALIFICATIONS feature to 
find out whether Language is required for the job or not.Keywords that is used for language searching are 'Java','C++' 
or 'Python'.(There case should not be changed). 

Output Format :
Language Count
"""


# Solution


import csv  # Importing the CSV module

# Dictionary to track the count of each programming language
lang = {'Java': 0, 'C++': 0, 'Python': 0}

# Open the dataset file in read mode
with open("amazon_jobs_dataset.csv", "r", encoding="utf-8") as fileObj:
    reader = csv.DictReader(fileObj, skipinitialspace=True)  # Read CSV file as a dictionary

    for row in reader:
        # Extract and clean the location
        location = row.get("location", "").strip().lower()

        # Split the location into individual parts
        location_parts = [part.strip() for part in location.split(",")]

        # Ensure job location is in India by checking if 'in' is mentioned
        if location_parts and location_parts[0] != "in":
            continue

        # Extract the qualifications column
        basic_qualifications = row.get("BASIC QUALIFICATIONS", "").strip()

        # Check if the job requires a Bachelor's degree
        if "Bachelor" in basic_qualifications or "BS" in basic_qualifications or "BA" in basic_qualifications:
            # Count occurrences of each programming language
            if "Java" in basic_qualifications:
                lang["Java"] += 1
            if "C++" in basic_qualifications:
                lang["C++"] += 1
            if "Python" in basic_qualifications:
                lang["Python"] += 1

# Find the most in-demand programming language
most_demanded_lang = max(lang, key=lang.get)
print(most_demanded_lang, lang[most_demanded_lang])
