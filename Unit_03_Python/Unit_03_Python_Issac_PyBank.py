import os
import csv
csvpath = r"C:\Users\Owner\Desktop\SMU_Assignments\Unit_03_Python\Instructions\PyBank\Resources\budget_data.csv"


months = 0
profit_losses = 0
avg_changes = []

lastRowProfit = 0
currRowProfit = 0
isFirstRow = True

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        months = months + 1
        profit_losses = profit_losses + int(row[1])

        currRowProfit = int(row[1])

        if (isFirstRow == True):
            lastRowProfit = currRowProfit
            isFirstRow = False
        else:
            change = currRowProfit - lastRowProfit
            avg_changes.append(change)
            lastRowProfit = currRowProfit

#Total number of months in dataset
print(f"Total Months: {months}")

#Net total amount of "Profit/Losses" over entire period
print(f"Total: {profit_losses}")

#Average of changes in "Profit/Losses" over entire period
#print(profit_losses/months) # average = total / number of months

print(f"Average Change: {sum(avg_changes)/len(avg_changes)}")

#Greatest increase in profit (date and amount)
print(f"Greatest Increase in Profit: {max(avg_changes)}")

#Greatest decrease in losses (date and amount)
print(f"Greatest Decrease in Profit: {min(avg_changes)}")
