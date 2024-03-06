import csv

with open("pi_leaderboard.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    rows = list(reader)  # Convert iterator to list

# Sort the rows based on the scores (assuming the scores are in the second column)
rows.sort(key=lambda x: int(x[1]), reverse=True)

# Get the top five highest scorers
top_five = rows[:5]

# Print the top five highest scorers
for rank, (name, score, class_) in enumerate(top_five, start=1):
    print(f"Rank {rank}: Name: {name}, Score: {score}, Class: {class_}")