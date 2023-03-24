import csv
election_data_csv = "election_data.csv"

totalvotes = 0
can = []
vpc = {}
winningcan = ""
winningvotes = 0

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        totalvotes += 1
        candidate = row[2]

        if candidate not in can:
            can.append(candidate)
            vpc[candidate] = 0
        vpc[candidate] += 1

with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalvotes}\n")
    txtfile.write("-------------------------\n")

    for candidate in vpc:
        votes = vpc[candidate]
        percentage = round(votes/totalvotes * 100, 2)
        txtfile.write(f"{candidate}: {percentage}% ({votes})\n")

        if votes > winningvotes:
            winning_candidate = candidate
            winning_votes = votes

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write("-------------------------\n")

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

for candidate in vpc:
    votes = vpc[candidate]
    percentage = round(votes/totalvotes * 100, 2)
    print(f"{candidate}: {percentage}% ({votes})")

    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes

print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")