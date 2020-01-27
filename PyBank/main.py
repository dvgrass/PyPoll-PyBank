# Import dependencies for PyBank analysis

import os
import csv

# Join for files to load/export

bank_csv = os.path.join("Resources", "budget.csv")
bank_txt = os.path.join("analysis", "budget_analysis.txt")

# Establish Parameters

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ['', 999999999999]
total_net = 0

with open(bank_csv) as bank_data:
    reader = csv.reader(bank_data)
    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_months + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        months_of_change = month_of_change + [row[0]]

                # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
