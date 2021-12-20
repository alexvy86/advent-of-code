counts = dict()

with open('day5.input') as f:
    for line in f.read().split("\n"):
        [(x_start, y_start), (x_end, y_end)] = [(int(num) for num in coord.split(",")) for coord in line.split(" -> ")]

        if x_end == x_start:
            x_array = [x_start]*(abs(y_end-y_start) + 1)
        elif x_end > x_start:
            x_array = range(x_start, x_end + 1, 1)
        else:
            x_array = range(x_start, x_end - 1, -1)

        if y_end == y_start:
            y_array = [y_start]*(abs(x_end-x_start) + 1)
        elif y_end > y_start:
            y_array = range(y_start, y_end + 1, 1)
        else:
            y_array = range(y_start, y_end - 1, -1)

        for key in (f"{x}_{y}" for x,y in zip(x_array, y_array)):
            counts[key] = counts.get(key, 0) + 1

print(len([c for c in counts.values() if c > 1]))
