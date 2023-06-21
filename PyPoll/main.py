import csv
import os
import pandas as pd
import sys

# File paths
csv_path = "../PyPoll/Resources/election_data.csv"
output_folder = "../PyPoll/Analysis"
output_file = os.path.join(output_folder, "election_results.txt")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# ------------------------------------------------------------
# Count the number of active rows in column A (excluding the first row)
total_votes = len(df)

print("Election Results")
print("---------------------------")
# Print the total votes
print("Total Votes:", total_votes)
print("---------------------------")

# ------------------------------------------------------------
# Step 1: Find all the different names in COLUMN C
unique_names = df["Candidate"].unique()

# Step 2.1: Count the total number of active rows in COLUMN A
total_votes2 = len(df) - 1

# Step 2.2 & 2.3: Count the total number of rows and calculate the percentages for each name
results = []
for name in unique_names:
    rows = len(df[df["Candidate"] == name])
    percentage = (rows / total_votes2) * 100
    results.append((name, percentage, rows))

# Step 3: Print the results
for result in results:
    name, percentage, rows = result
    print(f"{name}: {percentage:.2f}% ({rows})")
# ------------------------------------------------------------
print("---------------------------")

# Task 4: Find the winner
max_percentage = 0
winner = None

for result in results:
    name, percentage, _ = result
    if percentage > max_percentage:
        max_percentage = percentage
        winner = result

# Task 5: Print the winner's name
print("Winner:", winner[0])

print("---------------------------")
# ------------------------------------------------------------

# Export the terminal output to a text file
with open(output_file, "w") as f:
    # Redirect the standard output to the file
    original_stdout = sys.stdout
    sys.stdout = f

    print("Election Results")
    print("---------------------------")
    print("Total Votes:", total_votes)
    print("---------------------------")

    for result in results:
        name, percentage, rows = result
        print(f"{name}: {percentage:.2f}% ({rows})")

    print("---------------------------")
    print("Winner:", winner[0])
    print("---------------------------")

    # Restore the standard output
    sys.stdout = original_stdout

print("Results exported to:", output_file)
