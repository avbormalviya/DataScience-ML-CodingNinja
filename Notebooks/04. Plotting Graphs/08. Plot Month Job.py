# Problem statement

"""
Given File:
amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018.
This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the Bar graph between Month vs Job Openings.

Print the month name and the number of job posting as integer value.

Order of months doesn't matter.

Output Format :
month_name1 job_posting1
month_name2 job_posting2
...
...
...
"""

# Solution


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("amazon_jobs_dataset.csv")

# Convert Posting_date to datetime and extract month names
df["month"] = pd.to_datetime(df["Posting_date"], errors='coerce').dt.month_name()

# Drop NaN values
df.dropna(subset=["month"], inplace=True)

# Plot bar chart
plt.figure(figsize=(10, 6))
df["month"].value_counts().sort_index().plot(kind="bar", color='skyblue', edgecolor='black')

# Labels & Title
plt.xlabel("Month", fontsize=12)
plt.ylabel("Number of Job Postings", fontsize=12)
plt.title("Amazon Job Postings by Month", fontsize=14)
plt.xticks(rotation=45)  # Rotate month labels for clarity
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show plot
plt.show()

# Print month-wise job counts
print(df["month"].value_counts().sort_index())
