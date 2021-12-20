lines = []
counts = dict()

with open('day5.input') as f:
    for l in f.read().split("\n"):
        lines.append([[int(c) for c in x.split(",")] for x in l.split(" -> ")])

#print(lines)

for line in lines:
    if line[0][0] == line[1][0]:
        x = line[0][0]
        s = line[0][1] if line[0][1] < line[1][1] else line[1][1]
        e = line[0][1] if line[0][1] > line[1][1] else line[1][1]
        for y in range(s, e+1):
            key = f"{x}_{y}"
            counts[key] = counts.get(key, 0) + 1
    elif line[0][1] == line[1][1]:
        y = line[0][1]
        s = line[0][0] if line[0][0] < line[1][0] else line[1][0]
        e = line[0][0] if line[0][0] > line[1][0] else line[1][0]
        for x in range(s, e+1):
            key = f"{x}_{y}"
            counts[key] = counts.get(key, 0) + 1
    else:
        s_x, s_y = line[0]
        e_x, e_y = line[1]
        step_x = 1 if e_x > s_x else -1
        step_y = 1 if e_y > s_y else -1
        if step_x == 1:
            e_x += 1
        else:
            e_x -= 1
        if step_y == 1:
            e_y += 1
        else:
            e_y -= 1
        for x,y in zip(range(s_x, e_x, step_x), range(s_y, e_y, step_y)):
            key = f"{x}_{y}"
            counts[key] = counts.get(key, 0) + 1

#print(counts.items())
print(len([c for c in counts.values() if c > 1]))
