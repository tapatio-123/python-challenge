import os
import csv 

budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    total = 0
    months = 0
    sum_change = 0
    previous = 0



    for row in csvreader: 
        total = total + float (row[1])
        months = months + 1

        change = float (row[1])
        sum_change = sum_change + change

        average = sum_change / (total - 1)

print (f"Total Months: {months}")
print (f"Total: ${total}")
print (f"Average Change: ${average}")
#print (f"Greatest Increase in Profits: {}")
#print (f"Greatest Decrease in Profits: {}")



with open("output.txt", "w") as txt_file:
    txt_file.write(f"Total months: {months}")
    txt_file.write(f"Total: {total}")
    txt_file.write(f"Average Change: {average}")
    #txt_file.write(f"Greatest Increase in Profits: {}")
    #txt_file.write(f"Greatest Decrease in Profits: {}")
