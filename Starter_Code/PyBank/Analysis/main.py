# Import data for the analysis
import os
import csv

# Set the path for csv file
budget_data=os.path.join('Resources', 'budget_data.csv')

# count the total number of months
total_months = 0

# count the total profit and loss
total_profit_loss = 0

# count the output value of total profit and loss
value = 0

# count the output value of total profit and loss
change = 0

# A list to hold the dates of the financial records
dates = []

# A list to hold the profits/loss
profits = []

# Read csv file
with open(budget_data, newline="") as budget:
    csvreader = csv.reader(budget, delimiter=",")
    # Reading header row
    csv_header = next(csvreader)
    # Go to the first row


    first_row = next(csvreader)

    # Add total month counter

    total_months += 1

    # Add profit and loss counter
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])

    # Read the rows after the header row
    for row in csvreader:

        # Get the date
        dates.append(row[0])

        # Keep the the records of changes in rows
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        # Total number of months
        total_months += 1

        # The net total amount of profit/ losses over the entire period
        total_profit_loss = total_profit_loss + int(row[1])

        # Average of the changes in "Profit/Losses" over the entire period
        avg_change = sum(profits)/len(profits)

  # The greatest increase in profits
    greatest_increase = max(profits)
    greatest_inc_index = profits.index(greatest_increase)
    greatest__inc_date = dates[greatest_inc_index]

    # The greatest decrease in profits
    greatest_decrease = min(profits)
    greatest__dec_index = profits.index(greatest_decrease)
    greatest__dec_date = dates[greatest__dec_index]

#Print the analysis output
printoutput = (
    f"Financial Analysis\n"
    f"-------------------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_profit_loss)}\n"
    f"Average Change: ${str(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})\n")
print(printoutput)

# Exporting text file

output_file = os.path.join('Analysis', 'pyBank_output.txt')


pyBankoutput = open(output_file, "w")

line1 = "Financial Analysis"
line2 = "------------------------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})")
line7 = str(
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})")
pyBankoutput.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7))







