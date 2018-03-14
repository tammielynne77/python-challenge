import os
import csv


Voter_ID = []
County = []
Candidate = []

with open('election_data_2.csv', newline="") as csvfile:
    ignore = csvfile.readline()
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])


Total_Votes = len(Voter_ID)

Dict_Candidate_Count = dict((x,Candidate.count(x)) for x in set(Candidate))   

List_Candidate_Names = (list(Dict_Candidate_Count.keys()))
List_Candidate_Votes = (list(Dict_Candidate_Count.values()))

Percentage_of_Votes = ["{:.2%}".format(x/Total_Votes) for x in (List_Candidate_Votes)]

Highest_Vote = max(List_Candidate_Votes)
Index_Winner = List_Candidate_Votes.index(Highest_Vote)

print("Election Results")
print("Total Votes:", Total_Votes)
print("Winner:", List_Candidate_Names[Index_Winner])
print("Winner Vote Total:", Highest_Vote)
print("Winner Percentage of Votes:", Percentage_of_Votes[Index_Winner])