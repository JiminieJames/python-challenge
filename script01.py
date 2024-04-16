import csv
import os

# Set path for file
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# Define variables to store financial analysis results
total_months = 0
total_profit_losses = 0
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the data from the CSV file
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    # Initialize variables to track the previous month's profit/loss
    previous_profit_loss = None

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract the date and profit/loss for the current row
        date = row[0]
        profit_loss = int(row[1])

        # Increment the total number of months
        total_months += 1

        # Add the profit/loss to the total
        total_profit_losses += profit_loss

        # Calculate the change in profit/loss from the previous month
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            monthly_changes.append(change)

            # Update the greatest increase and decrease if applicable
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        # Update the previous month's profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(monthly_changes) / len(monthly_changes)

# Print the financial analysis results
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
