instructions = []
with open('day2.input') as f:
    for line in f:
        pieces = line.split()
        instructions.append( (pieces[0], int(pieces[1])) )

# pylint: disable=invalid-name
aim = 0
horizontal_coord = 0
vertical_coord = 0
# pylint: enable=invalid-name

for i in instructions:
    if i[0] == 'forward':
        horizontal_coord += i[1]
        vertical_coord += aim * i[1]
    elif i[0] == 'down':
        aim += i[1]
    elif i[0] == 'up':
        aim -= i[1]

print(horizontal_coord * vertical_coord)
