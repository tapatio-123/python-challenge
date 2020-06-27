import os
import csv

election_csv = os.path.join("..","PyPoll", "Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")


    csv_header = next(csvreader)

votes = 0
candidates = {}

for row in csvreader: 
    total = total + float (row[1])
    votes = votes + 1
    
    if row [2] in candidates:

        pass

    else:
        pass 
for key, value in candidates.items ():

    print(f"{key}: + {value}")

    print (f"Total votes: {votes}")


with open("output.txt", "w") as txt_file:
    txt_file.write(f"Total votes: {votes}")
   