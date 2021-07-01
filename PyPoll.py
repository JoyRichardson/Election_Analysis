# Add our dependencies.
import csv
import os

# Assign a variable to load a file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare a new list
candidate_options = []

# Create a dictionary
candidate_votes = {}

# Declare winning components
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes +=1

        # Print candidate names from each row
        candidate_name = row[2]

        # If the candidate does not match an existing candidate
        if candidate_name not in candidate_options:

            # Add to candidate list
            candidate_options.append(candidate_name)
        
            # Track candidate vote count
            candidate_votes[candidate_name] = 0

        # Add votes to candidate count
        candidate_votes[candidate_name] += 1

# Save results to a text file
with open(file_to_save, "w") as txt_file:

    # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

# Calculate percentage of votes per candidate
#Iterate through the list
    for candidate_name in candidate_votes:

        # Get vote count of candidate
        votes = candidate_votes[candidate_name]

        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do - print each name, count and percentage to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        # Save candidate results to the text file
        txt_file.write(candidate_results)
            
        # Determine winning vote count for candidate
        # Calcaulate if votes > winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If yes, then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            
            # And set winning_candidate = candidate name
            winning_candidate = candidate_name
        
    # Print winning name, count and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


# Print the candidate vote dictionary
print(candidate_votes)


# 1 The total number of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won
# 4 The total number of votes each candidate won
# 5 The winner of the election based on popular vote