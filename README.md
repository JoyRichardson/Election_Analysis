# An Analysis of Election Results
## Overview of Election Audit
Tom and Seth work at the Colorado Board of Elections and would like to have recent election results audited and a report certifying the results.  This should include the following:
* The total number of votes cast
* A complete list of candidates who received votes
* The total number of votes each candidate won
* The percentage of votes each candidate won
* The winner of the election based on popular vote
## Resources
Data:  election_results.csv file <br/>
Software(s):  Python 3.7 and Visual Studio Code 1.57.1
## Results
Our analysis of the election showed the following results:
### Votes Cast in the Election
Total votes were 369,711
### Results by County
The County of Denver had the largest number of votes with voter participation as follows:<br/>
Jefferson:  10.5% (38,855 votes)<br/>
Denver: 82.8% (306,055 votes)<br/>
Arapahoe: 6.7% (24,801 votes)<br/>
### Candidates
Charles Casper Stockham <br/>
Diana DeGette <br/>
Raymon Anthony Doane <br/>
### Results by Candidate
Charles Casper Stockham received 23.0% of the vote with 85,213 votes. <br/>
Diana DeGette received 73.8% of the vote with 272,892 votes. <br/>
Raymon Anthony Doane received 3.1% of the vote with 11,606 votes. <br/>
### Declared Winner
Diana DeGette who received 73.8% of the vote with 272,892 votes.

## Challenges
This was a complex analysis, extracting data for both candidates and counties, and performing numerous calculations.  We have listed the steps involved below for your review:
* imported our dependencies and created paths to our source and output files
* initialized a total vote counter
* defined lists and dictionaries for candidates and counties
* created variables for winners, counts and percentages for candidates and counties
* used `for` loop to iterate through the data to extract cnadidate and county names
* nested `if` statements in the `for`loop to add candidate and county names to the list and count the votes for both
* used `for` loops to retrieve the vote count and calculate the percentages of votes for candidates and counties
* nested `if` statements in the `for` loops to determine the winning candidate and the county with the largest turnout
* saved the results to a text file
* printed final counts to the terminal

## Summary
While our analysis was on a local congressional election, the code could easily be updated for other purposes.

This macro uses variables to load and save files from and to a specific path.  Similar to what we did previously in VBA, we could add a function to create an input field 
that would redirect to other files.
```python
# Add a variable to load a file from a path.
file_to_load = os.path.join(".","Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join(".","Analysis", "election_analysis.txt")
```
This macro also uses several variables referencing counties that could be updated to reference cities (or other jurisdications) with minimal effort.  For example, you would replace 'county' with 'city' in these code sections:

```python
# 1. Create a county list and county votes dictionary.
county_list = []
county_votes = {}
```

```python
# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_turnout = 0
largest_percentage = 0
```

```python
# 3: Extract the county name from each row.
        county_name = row[1]
```

```python
# 4a: If the county does not match any existing county in the county list
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
```
            
```python
 # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```

```python
# Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
```

```python
# 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        count=county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        count_percentage=float(count)/float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results=(f"{county_name}: {count_percentage:.1f}% ({count:,})\n")

        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if(count > largest_turnout) and (count_percentage > largest_percentage):
            largest_turnout = count
            largest_percentage = count_percentage
            largest_county = county_name
```

```python
   # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary =(
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)
```

```python
# 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)
```
