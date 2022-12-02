items = []
current_elfs_items = []
with open('day1.input') as f:
    for line in f.read().splitlines():
        if line == "":
            items.append(current_elfs_items)
            current_elfs_items = []
        else:
            current_elfs_items.append(int(line))

print(sum(sorted((sum(elfs_items) for elfs_items in items), reverse=True)[:3]))
