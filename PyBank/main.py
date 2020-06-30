import os
import csv 

budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    csv_header = next(csvreader)

    total = 0
    months = 0
    total_months = 0
    total_change = 0
    datelist = []
    pl_list = []
   
    for row in csvreader:
        datelist.append(row[0])
        pl_list.append(int(row[1]))
        total = total + float (row[1])
        months = months + 1
    
    delta = []
    total_months = len(datelist)
    for i in range(1,total_months):
        delta.append(pl_list[i]-pl_list[i-1])
    
    inc_pl = max(delta)
    dec_pl = min(delta)

    inc_date = datelist[delta.index(max(delta))+1]
    dec_date = datelist[delta.index(min(delta))+1]
    
    average = sum(delta)/(total_months-1)

average = '${:.2f}'.format(average)

print (f"Total Months: {total_months}")
print (f"Total: ${total}")
print (f"Average Change: {average}")
print (f"Greatest Increase in Profits: {inc_date} (${inc_pl})")
print (f"Greatest Decrease in Profits: {dec_date} (${dec_pl})")

with open("output.txt", "w") as txt_file:
    txt_file.write(f"Total months: {months}\n")
    txt_file.write(f"Total: {total}\n")
    txt_file.write(f"Average Change: {average}\n")
    txt_file.write(f"Greatest Increase in Profits: {inc_date} (${inc_pl})\n")
    txt_file.write(f"Greatest Decrease in Profits: {inc_date} (${dec_pl})")
