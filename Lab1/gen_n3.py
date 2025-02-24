import itertools


# Định nghĩa sở thích của người chơi
def generate_preferences():
    players_A = ["A1", "A2", "A3"]
    players_B = ["B1", "B2", "B3"]

    # Tạo tất cả các cách sắp xếp cho sở thích của A và B
    preferences_A = list(itertools.permutations(players_B))
    preferences_B = list(itertools.permutations(players_A))

    return players_A, players_B, preferences_A, preferences_B


# Hàm kiểm tra sự ổn định của một cặp đôi
def is_stable(matching, preferences_A, preferences_B):
    for a, b in matching:
        for c, d in matching:
            if a != c and b != d:  # Đảm bảo không so sánh cùng một cặp
                # Kiểm tra nếu cặp (a, b) không ổn định
                if preferences_A[a].index(b) > preferences_A[a].index(
                    d
                ) and preferences_B[b].index(a) > preferences_B[b].index(c):
                    return False
    return True


# Tạo tất cả các khả năng ghép đôi
def generate_matchings(players_B):
    return itertools.permutations(players_B)


# Kiểm tra tất cả các khả năng ghép đôi
def check_stable_matchings():
    players_A, players_B, preferences_A_list, preferences_B_list = (
        generate_preferences()
    )
    # print(players_A, players_B, preferences_A_list, preferences_B_list)
    answer = []
    preferences_A_list1 = []
    preferences_B_list1 = []
    for preferences_A1 in preferences_A_list:
        for preferences_A2 in preferences_A_list:
            for preferences_A3 in preferences_A_list:
                preferences_A_list1.append(
                    [preferences_A1, preferences_A2, preferences_A3]
                )
    for preferences_B1 in preferences_B_list:
        for preferences_B2 in preferences_B_list:
            for preferences_B3 in preferences_B_list:
                preferences_B_list1.append(
                    [preferences_B1, preferences_B2, preferences_B3]
                )
    # Kiểm tra tất cả các cách sắp xếp sở thích
    for preferences_A in preferences_A_list1:
        for preferences_B in preferences_B_list1:
            # print(preferences_A, preferences_B)
            current_preferences_A = {
                players_A[i]: list(preferences_A[i]) for i in range(len(players_A))
            }
            current_preferences_B = {
                players_B[i]: list(preferences_B[i]) for i in range(len(players_B))
            }
            # print(current_preferences_A, current_preferences_B)
            check = True
            for matching in generate_matchings(players_B):
                current_matching = list(zip(players_A, matching))
                if not is_stable(
                    current_matching, current_preferences_A, current_preferences_B
                ):
                    check = False
                    break
            if check:
                answer.append([current_preferences_A, current_preferences_B])

    return answer


# Chạy chương trình
answer = check_stable_matchings()

# In kết quả
if answer:
    print("Có các ghép đôi ổn định:")
    for kq in answer:
        print(kq)
else:
    print("No solution")
