instructions = []
with open('day2.input') as f:
    for line in f:
        pieces = line.split()
        instructions.append( (pieces[0], int(pieces[1])) )

horizontal_coord = 0
vertical_coord = 0
for i in instructions:
    if i[0] == 'forward': horizontal_coord += i[1]
    elif i[0] == 'down': vertical_coord += i[1]
    elif i[0] == 'up': vertical_coord -= i[1]

print(horizontal_coord * vertical_coord)
