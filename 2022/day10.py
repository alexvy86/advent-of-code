register = 1
current_cycle = 0
total_signal_strength = 0

screen = [['.']*40,['.']*40,['.']*40,['.']*40,['.']*40,['.']*40]

def print_pixel():
    r = current_cycle // 40
    col = current_cycle % 40
    char = '#' if (current_cycle % 40) + 1 in range(register, register + 3) else '.'
    screen[r][col] = char

with open('day10.input') as f:
    for line in f.read().splitlines():
        (op, arg) = (line, 0) if line == "noop" else line.split(" ")

        if (current_cycle + 1) in [20,60,100,140,180,220]:
            total_signal_strength += (current_cycle + 1) * register

        print_pixel()

        if op == "noop":
            current_cycle += 1
        elif op == "addx":
            current_cycle += 1

            if (current_cycle + 1) in [20,60,100,140,180,220]:
                total_signal_strength += (current_cycle + 1) * register
            print_pixel()

            current_cycle += 1
            register += int(arg)
        else:
            raise ValueError(f"Unsupported operation {op}")

print(total_signal_strength)
for row in screen:
    print("".join(row))
