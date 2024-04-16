import csv
import os

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis.txt")

# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# Defining variables for later review

# We will be counting months and P&l so we set those to zero
totalmonths = 0
totalpl = 0
# Want to have an open array to add information to.
monthly_changes = []
# this variable requires two values, date and amount. learned from AI tool.
greatincrease = ["", 0]
greatdecrease = ["", 0]

# Read the data from the CSV file, copied from lecture
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)  # Skip the header row from lecture

    # Initialize variables to track the previous month's profit/loss
    previousprofitloss = 0

    # A for loop to go over all of the sheet
    for row in csv_reader:
        # the date is in the 1st column(0) and the profit/ loss is in the second (1)
        date = row[0]
        # has to be an integer so we can count it
        profit_loss = int(row[1])

        # counting the total months
        totalmonths = totalmonths + 1

        # Add the profit/loss to the total
        totalpl = totalpl + profit_loss

        #I tried a lot to get this to work and think I just stummbled into this one. 
        if previousprofitloss:
            changed = profit_loss - previousprofitloss
            monthly_changes.append(changed)

            # Like we did with VBA we are updating our current greatest increase and decrease as they are found
            if changed > greatincrease[1]:
                greatincrease = [date, changed]
            elif changed < greatdecrease[1]:
                greatdecrease = [date, changed]

        # Update the previous month's profit/loss
        previousprofitloss = profit_loss

# We learned in activity this week, and we need a len of the months so we can get Sum divided number of months for a average
average_change = sum(monthly_changes) / len(monthly_changes)

# Print the financial analysis results
output = (f"Financial Analysis\n" 
        f"------------------------------\n"   
        f"Total Months: {totalmonths}\n"
        f"Total: ${totalpl}\n"
        f"Average Change: ${average_change:.2f}\n"  
        f"Greatest Increase in Profits: {greatincrease[0]} (${greatincrease[1]})\n"
        f"Greatest Decrease in Profits: {greatdecrease[0]} (${greatdecrease[1]})\n"
        f"------------------------------"
        )  
#test print
# print(output)

#Learned from Megan the TA
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

# Output Findings to Text file
