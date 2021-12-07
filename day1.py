num_of_increases = 0
last_value = None
with open('day1.input') as f:
    for depth in (int(line) for line in f):
        if last_value is not None and depth > last_value:
            num_of_increases += 1
        last_value = depth

print(num_of_increases)
