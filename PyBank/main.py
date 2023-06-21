import csv
import os
import pandas as pd

# File paths
csv_path = "../PyBank/Resources/budget_data.csv"
output_folder = "../PyBank/Analysis"
output_file = os.path.join(output_folder, "financial_analysis.txt")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# ----------------------------------------------
# Extract the "Date" column from the DataFrame
dates = df["Date"]

# Count the number of unique months
month_count = len(dates.unique())

# print("Total Months:", month_count)

# ----------------------------------------------
# Calculate the net total by summing the values in the "Profit/Losses" column
net_total = df["Profit/Losses"].sum()

# print("Total: $", net_total)

# ----------------------------------------------
# Extract the "Profit/Losses" column from the DataFrame
profits_losses = df["Profit/Losses"]

# Calculate the difference between consecutive rows
differences = profits_losses.diff()

# Exclude the first row from the differences calculation
differences = differences[1:]

# Calculate the average of the differences
average_difference = differences.mean()

# Round the average difference to two decimal places
rounded_average_difference = round(average_difference, 2)

# print("Average Change:", rounded_average_difference)

# ----------------------------------------------
# Extract the "Date" and "Profit/Losses" columns from the DataFrame
# VARIABLES - dates = df["Date"]
# VARIABLES - profits_losses = df["Profit/Losses"]

# Calculate the differences between consecutive rows
differences = profits_losses.diff()

# Find the index of the row with the greatest increase in profits
max_increase_index = differences.idxmax()

# Get the corresponding date and amount
max_increase_date = dates[max_increase_index]
max_increase_amount = differences[max_increase_index]

# print("Greatest Increase in Profits:", max_increase_date, "($", max_increase_amount, ")")

# ----------------------------------------------
# Extract the "Date" and "Profit/Losses" columns from the DataFrame
# VARIABLES - dates = df['Date']
# VARIABLES - profits_losses = df['Profit/Losses']

# Calculate the differences between consecutive rows
differences = profits_losses.diff()

# Find the index of the row with the greatest decrease in profits
min_decrease_index = differences.idxmin()

# Get the corresponding date and amount
min_decrease_date = dates[min_decrease_index]
min_decrease_amount = differences[min_decrease_index]

# print("Greatest Decrease in Profits:", min_decrease_date, "($", min_decrease_amount, ")")

# ----------------------------------------------

# Print the analysis
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${rounded_average_difference}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount})")
print(f"Greatest Decrease in Profits: {min_decrease_date} (${min_decrease_amount})")

# Export the analysis to a text file
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {month_count}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${rounded_average_difference:.2f}\n")
    txtfile.write(
        f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount})\n"
    )
    txtfile.write(
        f"Greatest Decrease in Profits: {min_decrease_date} (${min_decrease_amount})\n"
    )

# Print confirmation
print(f"Analysis has been exported to {output_file}.")
