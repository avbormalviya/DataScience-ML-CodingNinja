# Problem statement

"""
Given File:
amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the line graph between no. of Job postings with respect to year.

Print the year and the number of job posting as integer value.

Note: Year should be in ascending order.

Output Format :
year1   job_posting1
year2   job_posting2
...
...
...
"""

# Solution


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("amazon_jobs_dataset.csv")

# Convert posting date to datetime, handling errors
df['Year'] = pd.to_datetime(df['Posting_date'], errors='coerce').dt.year

# Drop rows with invalid year values
df.dropna(subset=['Year'], inplace=True)
df['Year'] = df['Year'].astype('Int64')  # Ensure year is integer

# Count job postings per year
year_counts = df['Year'].value_counts().sort_index()

# Plot job postings over years with improvements
plt.figure(figsize=(8, 6))
plt.plot(year_counts.index, year_counts.values, marker='o', linestyle='--', color='blue', markersize=6, linewidth=2)

# Labels and title
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Job Postings", fontsize=12)
plt.title("Amazon Job Postings Over the Years", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)  # Add grid for readability
plt.xticks(rotation=45)  # Rotate x-axis labels if needed

# Show plot
plt.show()

print(year_counts)
