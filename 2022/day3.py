total_priority = 0
total_badge_priority = 0

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

with open('day3.input') as f:
    group = []
    for line in f.read().splitlines():
        group.append(line)

        if len(group) < 3:
            continue

        elf1 = set(group[0])
        elf2 = set(group[1])
        elf3 = set(group[2])

        for letter in elf1:
            if letter in elf2 and letter in elf3:
                if letter < 'a':
                    priority = ord(letter) - 38
                else:
                    priority = ord(letter) - 96
                # print(f"{letter} {priority}")
                total_badge_priority += priority
                break

        group.clear()

print(total_badge_priority)
