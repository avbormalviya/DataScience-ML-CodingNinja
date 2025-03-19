
# Problem statement

"""
Given File:
amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the Pie chart between Indian cities vs No. of job openings.

Print the Indian cities and %age of Job distribution in India up to 2 decimal places.

Note: %age of Job distribution should be in descending order.

Output Format :
city1 percentage1
city2 percentage2
...
...
...
"""


# Solution


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("amazon_jobs_dataset.csv")

# Split location column
locations = df["location"].str.split(", ", expand=True)

# Filter rows where the country is India ("IN")
india_jobs = locations[locations[0] == "IN"]

# Extract city names from the last column (avoiding index assumption errors)
india_city = india_jobs.iloc[:, -1].value_counts()

# Drop missing values (if any)
india_city.dropna(inplace=True)

# Pie chart visualization
plt.figure(figsize=(8, 8))  # Increase figure size
plt.pie(india_city, labels=india_city.index, autopct="%1.2f%%", startangle=90, colors=plt.cm.Paired.colors)
plt.title("Amazon Job Postings in Different Indian Cities")
plt.show()

# Calculate & Print city-wise percentages
percentages = india_city / india_city.sum() * 100

for city, percentage in zip(india_city.index, percentages):
    print(f"{city}: {percentage:.2f}%")
