class Node:
    def __init__(self, item_name, size):
        self.children = {}
        self.name = item_name
        self.size = size
    def addChild(self, child_name, child_node):
        self.children[child_name] = child_node
    def totalSize(self):
        total = self.size
        for (_, c) in self.children.items():
            total += c.totalSize()
        return total

root = Node("/", 0)
current_node = root
stack = []

with open('day7.input') as f:
    for line in f.read().splitlines():
        if line == "$ cd /":
            continue

        if line == "$ cd ..":
            current_node = stack.pop()
        elif line.startswith("$ cd"):
            dir_name = line[5:]
            stack.append(current_node)
            current_node = current_node.children[dir_name]
        elif line == "$ ls":
            continue
        else:
            (size_or_dir, name) = line.split(" ")
            if size_or_dir == "dir":
                current_node.children[name] = Node(name, 0)
            else:
                current_node.children[name] = Node(name, int(size_or_dir))

total_space = 70000000
needed_free_space = 30000000
current_free_space = total_space - root.totalSize()
min_size_of_dir_to_delete = root.totalSize()

dirs_to_check = [root]
sum_of_sizes = 0
while len(dirs_to_check) > 0:
    current_dir = dirs_to_check.pop()
    for (_, c) in current_dir.children.items():
        if c.size == 0: # It's a dir
            dir_size = c.totalSize()
            if dir_size < 100000:
                sum_of_sizes += dir_size
            dirs_to_check.append(c)
            if current_free_space + dir_size > needed_free_space and \
                dir_size < min_size_of_dir_to_delete:
                min_size_of_dir_to_delete = dir_size

print(sum_of_sizes)
print(min_size_of_dir_to_delete)
