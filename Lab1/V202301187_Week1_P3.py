n = int(input())
students = {}
for i in range(n):
    tmp = list(input().split())
    key = tmp[0]
    tmp = tmp[1:]
    students[key] = tmp

m = int(input())

TAs = {}
for i in range(m):
    tmp = list(input().split())
    key = tmp[0]
    tmp = tmp[1:]
    TAs[key] = tmp

k = int(input())


def gale_shapey_extension(students, TAs, k):
    """
    Extend the Gale-Shapley algorithm to match students with TAs based on preferences.

    Parameters:
    students (dict): A dictionary where keys are student names and values are lists of preferred TAs.
    TAs (dict): A dictionary where keys are TA names and values are lists of preferred students.
    k (int): The maximum number of students each TA can handle.

    Returns:
    dict: A dictionary with student names as keys and their assigned TA as values.
          If a student is unmatched, the value is "unmatch".
    """
    proposers = list(students.keys())
    pts = {s: -1 for s in students.keys()}
    answer = {}
    M = {ta: [] for ta in TAs.keys()}
    while proposers:
        s = proposers.pop(0)
        for idx in range(pts[s] + 1, len(students[s])):
            pts[s] += 1
            ta = students[s][idx]
            if s in TAs[ta]:
                if len(M[ta]) < k:
                    M[ta].append(s)
                    break
                else:
                    max_current_s = k - 1
                    for i in range(k):
                        s1 = M[ta][i]
                        s2 = M[ta][max_current_s]
                        if TAs[ta].index(s1) > TAs[ta].index(s2):
                            max_current_s = i

                    s1 = M[ta][max_current_s]

                    if TAs[ta].index(s) < TAs[ta].index(s1):
                        M[ta][max_current_s] = s
                        proposers.append(s1)
                        break
    for s in students.keys():
        answer[s] = "unmatch"
    for ta in M:
        for s in M[ta]:
            answer[s] = ta
    return answer


print(gale_shapey_extension(students, TAs, k))
