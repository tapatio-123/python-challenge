

import os
import csv 
#importing file
budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#read into file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    csv_header = next(csvreader)
#setting variablbes
    total = 0
    total_months = 0
    total_change = 0
    datelist = []
    pl_list = []

#creating for loop to create list from csv data
    for row in csvreader:
        datelist.append(row[0]) #list for dates
        pl_list.append(int(row[1])) #profit loss list
        total = total + float (row[1]) #summing profit loss column


    delta = []
    total_months = len(datelist)
#for loop of differneces between profit/losses column
    for i in range(1,total_months):
        delta.append(pl_list[i]-pl_list[i-1])

#finding greatest increase/decrease in profits
    inc_pl = max(delta)
    dec_pl = min(delta)

#matching the above variables to column in csv file to get date
    inc_date = datelist[delta.index(max(delta))+1]
    dec_date = datelist[delta.index(min(delta))+1]
 
    average = sum(delta)/(total_months-1)

average = '${:.2f}'.format(average)

#writing out print statements
print (f"Total Months: {total_months}")
print (f"Total: ${total}")
print (f"Average Change: {average}")
print (f"Greatest Increase in Profits: {inc_date} (${inc_pl})")
print (f"Greatest Decrease in Profits: {dec_date} (${dec_pl})")

#creating text file
with open("output.txt", "w") as txt_file:
    txt_file.write(f"Total months: {total_months}\n")
    txt_file.write(f"Total: ${total}\n")
    txt_file.write(f"Average Change: {average}\n")
    txt_file.write(f"Greatest Increase in Profits: {inc_date} (${inc_pl})\n")
    txt_file.write(f"Greatest Decrease in Profits: {dec_date} (${dec_pl})")
