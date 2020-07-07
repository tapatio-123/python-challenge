import os
import csv
from collections import Counter

#importing file
election_csv = os.path.join("..","PyPoll", "Resources", "election_data.csv")
#reading into file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)
#setting variables
    candidates_list = []
    percentage = 0.0
    percent = []
    for row in csvreader: 
        candidates_list.append(row[2])#creating list of candidate names

    candidate_votes = Counter(candidates_list) #getting counts of votes for unique candidates
    candnames = list(candidate_votes.keys()) #setting keys from candidate_votes into list
    candvotes = list(candidate_votes.values()) #setting values from candidate_votes into list
    popular = max(candvotes)
    voters = len(candidates_list)

#writing out print statements

    print("Election Results")
    print(f"Total votes: {voters}")

#creating text file

with open("output.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write(f"Total votes: {voters}\n")

#creating for loop for formatting in text file
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
