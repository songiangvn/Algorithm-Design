# Read the number of students
n = int(input())

# Initialize preference lists for group A and B
A = [[] for _ in range(n + 1)]
B = [[] for _ in range(n + 1)]

# Initialize match arrays for group A and B
matchA = [-1 for _ in range(n + 1)]
matchB = [-1 for _ in range(n + 1)]

# Read preferences for group A
for i in range(1, n + 1):
    tmp = list(input().split())
    tmp = [int(item[-1]) for item in tmp]  # Extract the last character as integer
    A[i] = [-1 for _ in range(n + 1)]  # Initialize preferences for student i
    for j in range(1, n + 1):
        A[i][tmp[j - 1]] = j  # Set the preference for student i

# Read preferences for group B
for i in range(1, n + 1):
    tmp = list(input().split())
    tmp = [int(item[-1]) for item in tmp]  # Extract the last character as integer
    B[i] = [-1 for _ in range(n + 1)]  # Initialize preferences for student i
    for j in range(1, n + 1):
        B[i][tmp[j - 1]] = j  # Set the preference for student i

# Read the matching input
matching = list(input().split())
matching = [int(item[-1]) for item in matching]  # Extract the last character as integer

# Update matches based on the input
for i in range(0, 2 * n - 1, 2):
    matchA[matching[i]] = matching[i + 1]  # Match student to group A
    matchB[matching[i + 1]] = matching[i]  # Match student to group B


def check_stable_matching(A, B, matchA, matchB):
    """
    Check if the current matching is stable.

    A matching is considered stable if there are no pairs of students in groups A and B
    who would prefer each other over their current matches.

    Parameters:
    A (list): The preference list of group A.
    B (list): The preference list of group B.
    matchA (list): The current matches of group A.
    matchB (list): The current matches of group B.

    Returns:
    bool: True if the matching is stable, False otherwise.
    """
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Check if both students prefer each other over their current matches
            if A[i][j] < A[i][matchA[i]] and B[j][i] < B[j][matchB[j]]:
                return False  # Found an unstable pair
    return True  # All pairs are stable


# Check and return the stability of the matching
print(check_stable_matching(A, B, matchA, matchB))
