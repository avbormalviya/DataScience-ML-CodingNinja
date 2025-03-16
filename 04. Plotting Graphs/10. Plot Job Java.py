
# Problem statement

"""
Given File:
amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the scatter graph between year vs No. of jobs opening related to Java.

Print the year and number of Jobs opening in Java Profile.

Note: Use the Keyword 'Java' or 'java' in Basic Qualification feature for finding the job opening related to Java Profile. Print the year in ascending order.

Output Format :
year1 JobOpening1
year2 JobOpening2
...
...
...
"""


# Solution


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("amazon_jobs_dataset.csv")

# Filter Java-related job postings
java_jobs = df[df["BASIC QUALIFICATIONS"].str.contains("Java", case=False, na=False)].copy()

# Extract year from posting date
java_jobs["Year"] = pd.to_datetime(java_jobs["Posting_date"]).dt.year

# Count job postings per year
year_counts = java_jobs["Year"].value_counts().sort_index()

# Plot scatter graph with line
plt.figure(figsize=(10, 6))
plt.scatter(year_counts.index, year_counts.values, color="blue", s=100, label="Java Jobs")
plt.plot(year_counts.index, year_counts.values, linestyle="--", color="blue", alpha=0.6)

# Add data point labels
for x, y in zip(year_counts.index, year_counts.values):
    plt.text(x, y, str(y), fontsize=10, ha="right", va="bottom")

# Add labels, title, and grid
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Job Openings", fontsize=12)
plt.title("Java-Related Job Openings Over the Years", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.show()

# Print year-wise counts
print(year_counts)
