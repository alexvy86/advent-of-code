total_score = 0

def calculate_round_score(opponent, you):
    return 3 if you == opponent else 6 if you % 3 == (opponent + 1) % 3 else 0

with open('day2.input') as f:
    for line in f.read().splitlines():
        [opponent, you] = line.split()
        opponent_value = "ABC".index(opponent) + 1
        you_value = "XYZ".index(you) + 1
        # print (f"{opponent}({opponent_value}) {you}({you_value})")
        total_score += you_value + calculate_round_score(opponent_value, you_value)

print(total_score)
