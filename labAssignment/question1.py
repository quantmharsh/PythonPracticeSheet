
 # Create a list to store the scores of n colleges
scores = []

# Loop to read the scores of three parameters for each college
n=int(input("no of colleges"))
for i in range(n):
    print("Enter the scores of facilities, academics and infrastructure for college ", i+1)
    facility_score = int(input("facility score: 25/"))
    academics_score = int(input("academics score:50/"))
    infrastructure_score = int(input("infrastructure score:25/"))
    total_score = facility_score + academics_score + infrastructure_score
    scores.append(total_score)

# Sort the scores in descending order
scores.sort(reverse=True)

# Print the sorted scores
print("Total scores of colleges in descending order:")
for i in range(n):
    print("College ", i+1,scores[i])
