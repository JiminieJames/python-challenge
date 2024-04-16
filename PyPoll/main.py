import csv
import os

# Define the path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis.txt")

# Initialize variables to store vote counting results
total_votes = 0
candidate_votes = {}
candidates = set()

#Opening the file for date
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract the candidate name from the current row
        candidate = row[2]

        # Increment the total number of votes cast, learned this from ChatGPT
        total_votes += 1

        # Increment the vote count for the current candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

        # Add the candidate to the set of unique candidates
        candidates.add(candidate)

# Print the total number of votes cast
results1 = ("Election Results \n"
          "------------------------------\n"                
          f"Total Votes: {total_votes}\n"     
          "------------------------------")

top3=[]
# Calculate and print the results for each candidate
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    top3.append(f"{candidate}: {percentage:.3f}% ({votes})")
#I really could not figure out how to remove the funcion line from the printing between many sources.
results2 = "\n".join(top3)
# Determine the winner of the election
max_votes = 0
winner = ""
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate    
results3 = ("------------------------------\n"
            f"Winner: {winner}\n"
            "------------------------------")
results_combined = results1 + "\n" + results2 + "\n" + results3

#Learned from Megan the TA
with open(file_to_output, "w") as txt_file:
    txt_file.write(results_combined)