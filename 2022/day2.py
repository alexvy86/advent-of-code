total_score = 0

def calculate_round_score(opponent, you):
    return 3 if you == opponent else 6 if you % 3 == (opponent + 1) % 3 else 0

with open('day2.input') as f:
    for line in f.read().splitlines():
        [opponent, desired_result] = line.split()
        opponent_value = "ABC".index(opponent)
        you_value = opponent_value if desired_result == "Y" else \
                    (opponent_value - 1) % 3 if desired_result == "X" else \
                    (opponent_value + 1) % 3
        # print (f"{opponent}({opponent_value}) {you}({you_value})")
        shape_score = you_value + 1
        total_score += shape_score + calculate_round_score(opponent_value, you_value)

print(total_score)
