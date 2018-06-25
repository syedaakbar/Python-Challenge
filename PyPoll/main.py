# importing necessary modules
import csv
import os
import pdb       #for debugging

unique_list_candidates=[]
total_votes = 0

#creating the csv file path 
path_csv = os.path.join('election_data.csv')

#reading the csv using csv module and creating a file object
with open (path_csv,'r',newline = '') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    #skipping the header row 
    next(csv_reader)
    
    #creating a list of rows
    rows = list(csv_reader)
    total_votes = len(rows)

    for row in rows:

        # check if candidate is in unique list
        if row[2] not in unique_list_candidates:
            unique_list_candidates.append(row[2])

    max_candidate_vote=0
    max_candidate_name='' 
    results = []

    for candidate in unique_list_candidates:
        #pdb.set_trace()
        candidate_vote = 0

        for row in rows:
         
            if candidate == row[2]:
                 candidate_vote += 1
            else:
                percent_votes = (candidate_vote/total_votes)*100
                
        if candidate_vote > max_candidate_vote:
            max_candidate_vote = candidate_vote
            max_candidate_name = candidate

        results.append([candidate,candidate_vote,percent_votes])

# printing total votes, candidate's name, total votes and % of total votes received by candidates 
# printing the name of the winner of the elcetion poll
print('Election Results')
print("---------------------------------------")
print(f'Total Votes: {total_votes}')
print("---------------------------------------")
for value in results:
    print(f"{value[0]}: {value[1]} ({round(value[2],2)}%)")
print("---------------------------------------")
print(f'Winner: {max_candidate_name}')
print("---------------------------------------")

# saving the Election Results in a text file
fa = open('Election Results.txt','w') 
lines_of_text = ['Election Results \n', '-------------------------------------- \n', 
                 f'Total Votes: {total_votes} \n',
                 '-------------------------------------- \n']
fa.writelines(lines_of_text) 

for value in results:
    fa.write(f"{value[0]}: {value[1]} ({round(value[2],0)}%)\n")

fa.writelines(['-------------------------------------- \n',
                   f'Winner: {max_candidate_name} \n', 
                   '-------------------------------------- \n'])
fa.close() 