# Read the number of elements in both groups
n = int(input())

# Initialize match array and preference tracker for group 1
M = [-1 for _ in range(n)]  # Matches for group 2
pts = [-1 for _ in range(n)]  # Preference indices for group 1

# Initialize preference lists for both groups
group1 = [[] for _ in range(n)]  # Preferences for group 1
group2 = [[] for _ in range(n)]  # Preferences for group 2

# Read preferences for group 1
for i in range(n):
    group1[i] = list(map(int, input().split()))

# Read preferences for group 2 and initialize their preference ranking
for i in range(n):
    tmp = list(map(int, input().split()))
    group2[i] = [-1 for _ in range(n)]  # Initialize group 2 preferences
    for j in range(n):
        group2[i][tmp[j]] = j  # Set the preference index for group 2

# Initialize the list of proposers from group 1
proposers = [_ for _ in range(n)]

# While there are proposers in group 1
while proposers:
    h = proposers.pop(0)  # Get the next proposer from group 1
    for idx in range(pts[h] + 1, n):  # Iterate through preferences of proposer h
        pts[h] += 1  # Move to the next preference
        s = group1[h][idx]  # Get the current preference from group 1
        if M[s - n] == -1:  # If group 2 hasn't matched with anyone
            M[s - n] = h  # Match group 2's member s with proposer h
            break
        else:
            current_h = M[s - n]  # Get the current match for s
            # Check if the new proposer h is preferred over the current match
            if group2[s - n][h] < group2[s - n][current_h]:
                M[s - n] = h  # Update the match for s to h
                proposers.append(current_h)  # Re-add the current match to proposers
                break
    else:
        proposers.append(h)  # If no match found, re-add proposer h to the list

# Output the final matches
print(M)
