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

#print(counts.items())
print(len([c for c in counts.values() if c > 1]))
