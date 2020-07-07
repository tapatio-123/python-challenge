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

​    datelist.append(row[0])

​    pl_list.append(int(row[1]))

​    total = total + float (row[1])

​    months = months + 1

  

  delta = []

  total_months = len(datelist)

  for i in range(1,total_months):

​    delta.append(pl_list[i]-pl_list[i-1])

  

  inc_pl = max(delta)

  dec_pl = min(delta)



  inc_date = datelist[delta.index(max(delta))+1]

  dec_date = datelist[delta.index(min(delta))+1]

  

  average = sum(delta)/(total_months-1)



average = '${:.2f}'.format(average)



print (f"Total Months: {total_months}")

print (f"Total: ${total}")

print (f"Average Change: {average}")

print (f"Greatest Increase in Profits: {inc_date} {inc_pl}")

print (f"Greatest Decrease in Profits: {dec_date} {dec_pl}")



with open("output.txt", "w") as txt_file:

  txt_file.write(f"Total months: {months}\n")

  txt_file.write(f"Total: {total}\n")

  txt_file.write(f"Average Change: {average}\n")

  txt_file.write(f"Greatest Increase in Profits: {inc_date} {inc_pl}\n")

  txt_file.write(f"Greatest Decrease in Profits: {inc_date} {dec_pl}")







*****************



import os

import csv

from collections import Counter

\#from collections import Counter, OrderedDict



election_csv = os.path.join("..","PyPoll", "Resources", "election_data.csv")



with open(election_csv) as csvfile:

  csvreader = csv.reader(csvfile, delimiter= ",")

  csv_header = next(csvreader)



  \#votes = 0

  voters = []

  candidates_list = []

  c_tracker = 0 

  

  for row in csvreader: 

​    voters.append(row[1])

​    candidates_list.append(row[2])

​    c_tracker = (row[2].split(" "))



  candidate_votes = Counter(candidates_list)

  \#winner = candidate_votes.most_common(1)



  percentage = 0.0

  percent = []

  \#candvotes = []

  candnames = list(candidate_votes.keys())

  candvotes = list(candidate_votes.values())

  popular = max(candvotes)

  voters = len(candidates_list)

  print("Election Results")

  print (f"Total votes: {voters}")

  \#print(candvotes[2])

  for i in range (0,len(candvotes)):

​    percentage = (candvotes[i] / float(len(candidates_list)))

​    percent.append(percentage)

​    print ('{}:'.format(candnames[i]), "{:.2%}".format(percent[i]),'({})'.format(candvotes[i]))



  winner = candvotes.index(popular)

  



  \#for cand, votes in candidate_votes.values():

​    \#cl = cand

​    \#vl = votes

  \#percentage = ([(i,votes[i] / len(candidates_list)*100.0) for i in votes])





  \#percentage = ([(i,candidate_votes[i] / len(candidates_list)*100.0) for i, count in candidate_votes.most_common()])

  \#for cand, percentage in vote_percent.most_common(): 

  \#print(percentage)

  \#test = OrderedDict(candidate_votes.most_common())

  \#print(test)



  \#votes = votes + 1





  \#for i in candidate_votes:

​    \#print (i, candidate_votes[Khan])

  \#most_votes = 0



  \#if winner in candidates_list:

​    \#winner = most_votes



  \#percent = '{:.0%}'.format(candidates_list) 

  \#for cand, votes in candidate_votes.most_common():

​    \#print (votes)

​    \#print(votes)

  

  \#print(f"{dict(candidate_votes)}{percentage}")

  print(f"Winner: {candnames[winner]}")



with open("output.txt", "w") as txt_file:

  txt_file.write("Election Results\n")

  txt_file.write(f"Total votes: {voters}\n")

  \#txt_file.write(f"{dict(candidate_votes)}\n")

  txt_file.write(f"Winner: {winner}")

****************

import os

import csv

from collections import Counter

\#myfile = open('output.txt', 'a')



election_csv = os.path.join("..","PyPoll", "Resources", "election_data.csv")



with open(election_csv) as csvfile:

  csvreader = csv.reader(csvfile, delimiter= ",")

  csv_header = next(csvreader)



  voters = []

  candidates_list = []

  c_tracker = 0 

  

  for row in csvreader: 

​    voters.append(row[1])

​    candidates_list.append(row[2])

​    c_tracker = (row[2].split(" "))



  candidate_votes = Counter(candidates_list)



  percentage = 0.0

  percent = []

  candnames = list(candidate_votes.keys())

  candvotes = list(candidate_votes.values())

  popular = max(candvotes)

  voters = len(candidates_list)

  print("Election Results")

  print(f"Total votes: {voters}")

  \#myfile = open('output.txt', 'w')

with open("output.txt", "w") as txt_file:

  txt_file.write("Election Results\n")

  txt_file.write(f"Total votes: {voters}\n")



  for i in range (0,len(candvotes)):

​    percentage = (candvotes[i] / float(len(candidates_list)))

​    percent.append(percentage)

​    \#outputstr1 = '{}:'.format(candnames[i])

​    \#outputstr2 = "{:.1%}".format(percent[i])

​    \#outputstr3 = "({})".format(candvotes[i])

​    \#print(outputstr1 + " " + outputstr2 + " " + outputstr3)

​    outputstr = ('{}:'.format(candnames[i]), "{:.2%}".format(percent[i]),'({})'.format(candvotes[i]))

​    outputstr = ' '.join(outputstr)

​    print(outputstr)

​    txt_file.write(outputstr + "\n")

​    \#txt_file.write(outputstr1 + " " + outputstr2 + " " + outputstr3 + "\n")



​    \#myfile.write('{}:'.format(candnames[i]), "{:.2%}".format(percent[i]),'({})'.format(candvotes[i]))

​    \#myfile.close()

​    \#text_file.close()  

  candresults = candidate_votes.most_common()

  \#candresults = ('{}:'.format(candnames[i]), "{:.2%}".format(percent[i]),'({})'.format(candvotes[i]))

  winner = candvotes.index(popular)

  print(f"Winner: {candnames[winner]}")



\#with open("output.txt", "w") as txt_file:

  \#txt_file.write("Election Results\n")

  \#txt_file.write(f"Total votes: {voters}\n")

  \#txt_file.write(f"{outputstr}\n")

  txt_file.write(f"Winner: {candnames[winner]}")

  