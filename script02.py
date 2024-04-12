import csv
import os

# Define the path to the CSV file
csv_file = "election_data.csv"
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# Define variables to store vote counting results
total_votes = 0
candidate_votes = {}
candidates = set()

# Read the data from the CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract the candidate name from the current row
        candidate = row[2]

        # Increment the total number of votes cast
        total_votes += 1

        # Increment the vote count for the current candidate
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

        # Add the candidate to the set of unique candidates
        candidates.add(candidate)

# Print the total number of votes cast
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)

# Calculate and print the results for each candidate
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-" * 30)

# Determine the winner of the election
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")

print("-" * 30)