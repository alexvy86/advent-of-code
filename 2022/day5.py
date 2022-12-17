import re
from functools import reduce

def parse_move(l:str) -> list[int]:
    matches = re.match(r"move (\d+) from (\d+) to (\d+)", l)
    if matches is not None:
        return [int(x) for x in matches.groups()]
    return []

stacks = []
parsing_stacks = True

with open('day5.input') as f:
    for line in f.read().splitlines():
        if line == "":
            # Done parsing the stacks
            parsing_stacks = False
            for s in stacks:
                s.reverse() # Because we added the items from top to bottom as we parsed them
            continue

        if parsing_stacks:
            stack_line = re.findall(r"...? ?", line)
            # print(stack_line)
            current_stack_index = 1
            for item in stack_line:
                trimmed = item.strip()
                if trimmed == "1":
                    # Don't do anything for the line with stack indices
                    break
                if trimmed != "":
                    while len(stacks) <= current_stack_index:
                        stacks.append([])
                    stacks[current_stack_index].append(trimmed[1])
                current_stack_index += 1
        else:
            (how_many, src_stack, target_stack) = parse_move(line)
            for i in range(how_many):
                stacks[target_stack].append(stacks[src_stack].pop())

print(reduce(lambda acc, current: acc + current.pop(), stacks[1:], ""))
