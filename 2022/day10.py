register = 1
current_cycle = 1
total_signal_strength = 0
with open('day10.input') as f:
    for line in f.read().splitlines():
        arg = 0
        if line == "noop":
            op = line
        else:
            (op, arg) = line.split(" ")

        if current_cycle in [20,60,100,140,180,220]:
            total_signal_strength += current_cycle * register

        if op == "noop":
            current_cycle += 1
        elif op == "addx":
            current_cycle += 1

            if current_cycle in [20,60,100,140,180,220]:
                total_signal_strength += current_cycle * register

            current_cycle += 1
            register += int(arg)
        else:
            raise ValueError(f"Unsupported operation {op}")

print(total_signal_strength)
