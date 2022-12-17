import re

total_with_subsets = 0

with open('day4.input') as f:
    for line in f.read().splitlines():
        matches = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line)
        if matches is not None:
            a = int(matches.group(1))
            b = int(matches.group(2))
            c = int(matches.group(3))
            d = int(matches.group(4))
            if (a >= c and b <= d) or (c >= a and d <= b):
                total_with_subsets += 1

print(total_with_subsets)
