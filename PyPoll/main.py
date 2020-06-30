import os
import csv
from collections import Counter

election_csv = os.path.join("..","PyPoll", "Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)

    voters = []
    candidates_list = []
    percentage = 0.0
    percent = []
    
    for row in csvreader: 
        voters.append(row[1])
        candidates_list.append(row[2])

    candidate_votes = Counter(candidates_list)
    candnames = list(candidate_votes.keys())
    candvotes = list(candidate_votes.values())
    popular = max(candvotes)
    voters = len(candidates_list)
    print("Election Results")
    print(f"Total votes: {voters}")

with open("output.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write(f"Total votes: {voters}\n")

    for i in range (0,len(candvotes)):
        percentage = (candvotes[i] / float(len(candidates_list)))
        percent.append(percentage)
        outputstr = ('{}:'.format(candnames[i]), "{:.2%}".format(percent[i]),'({})'.format(candvotes[i]))
        outputstr = ' '.join(outputstr)
        print(outputstr)
        txt_file.write(outputstr + "\n")
   
    winner = candvotes.index(popular)
    print(f"Winner: {candnames[winner]}")
    txt_file.write(f"Winner: {candnames[winner]}")
