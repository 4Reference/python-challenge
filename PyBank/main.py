# Your task is to create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset

  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

  #```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# Set imports
import os
import csv

# Set variables and initialize
data = []


# Set and check path for CSV file script below assumes path origin is "python-challenge" folder
budgetData = os.path.join(".","PyBank","Resources","budget_data.csv")
currentDirectory = os.getcwd()
print(currentDirectory)
print(budgetData)

# Open the CSV file
with open(budgetData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    print(data[1])

    tmp = 0
    total = list()
    for i in range(0, row_count): 
        tmp = tmp + int(data[i][1]) 
    total.append(tmp) 
    diffTmp = list()
    k = int(data[1][1])
    #for j in range(2,row_count):
        #diffTmp = k - int(data[j][1]),
        #next(diffTmp)
        #k = int(data[j][1])
    #print(f"{diffTmp}")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total[0]:,}")


