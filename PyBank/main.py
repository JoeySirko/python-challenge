import csv
budgetcsv = "budget_data.csv"

totalmonths = 0
totalprofit = 0
preprofit = 0
profitchange = 0
profitdiff= []
months = []

with open(budgetcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        totalmonths += 1
        totalprofit += int(row[1])
        profitchange = int(row[1]) - preprofit
        preprofit = int(row[1])

        if totalmonths > 1:
            profitdiff.append(profitchange)
            months.append(row[0])

average_profit_change = sum(profitdiff) / len(profitdiff)

greatest_increase = max(profitdiff)
greatest_increase_date = months[profitdiff.index(greatest_increase)]

greatest_decrease = min(profitdiff)
greatest_decrease_date = months[profitdiff.index(greatest_decrease)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofit}")
print(f"Average Change: ${round(average_profit_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open('budget_analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {totalmonths}\n")
    f.write(f"Total: ${totalprofit}\n")
    f.write(f"Average Change: ${round(average_profit_change, 2)}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")