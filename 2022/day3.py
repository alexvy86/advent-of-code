total_priority = 0

with open('day3.input') as f:
    for line in f.read().splitlines():
        first_compartment = set(line[0:len(line)//2])
        second_compartment = set(line[len(line)//2:])

        for letter in first_compartment:
            if letter in second_compartment:
                if letter < 'a':
                    priority = ord(letter) - 38
                else:
                    priority = ord(letter) - 96
                # print(f"{letter} {priority}")
                total_priority += priority
                break

print(total_priority)
