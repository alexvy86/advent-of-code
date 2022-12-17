grid = []
with open('day8.input') as f:
    for line in f.read().splitlines():
        grid.append([int(x) for x in list(line)])

visible_tree_coords = set()

for (r, row) in enumerate(grid):
    max_height_from_left = -1
    max_height_from_right = -1
    for (c, height_from_left) in enumerate(row):
        # From left
        if height_from_left > max_height_from_left:
            visible_tree_coords.add((r,c))
            max_height_from_left = height_from_left
        # From right
        flipped_col_index = len(row) - 1 - c
        height_from_right = grid[r][flipped_col_index]
        if height_from_right > max_height_from_right:
            visible_tree_coords.add((r,flipped_col_index))
            max_height_from_right = height_from_right

for c in range(len(grid[0])):
    max_height_from_top = -1
    max_height_from_bottom = -1
    for (r, _) in enumerate(grid):
        # From top
        height_from_top = grid[r][c]
        if height_from_top > max_height_from_top:
            visible_tree_coords.add((r,c))
            max_height_from_top = height_from_top
        # From bottom
        flipped_row_index = len(grid) - 1 - r
        height_from_bottom = grid[flipped_row_index][c]
        if height_from_bottom > max_height_from_bottom:
            visible_tree_coords.add((flipped_row_index,c))
            max_height_from_bottom = height_from_bottom

print(len(visible_tree_coords))

def scenic_score(r, c) -> int:
    # Trees in the edges
    if r == 0 or r == len(grid) - 1:
        return 0
    if c == 0 or c == len(grid[0]) - 1:
        return 0

    score = 1
    # Look up
    current_r = r
    visible_trees = 0
    while current_r > 0:
        current_r -= 1
        visible_trees += 1
        if grid[current_r][c] >= grid[r][c]:
            break
    score *= visible_trees

    # Look down
    current_r = r
    visible_trees = 0
    while current_r < len(grid) - 1:
        current_r += 1
        visible_trees += 1
        if grid[current_r][c] >= grid[r][c]:
            break
    score *= visible_trees

    # Look left
    current_c = c
    visible_trees = 0
    while current_c > 0:
        current_c -= 1
        visible_trees += 1
        if grid[r][current_c] >= grid[r][c]:
            break
    score *= visible_trees

    # Look right
    current_c = c
    visible_trees = 0
    while current_c < len(grid[0]) - 1:
        current_c += 1
        visible_trees += 1
        if grid[r][current_c] >= grid[r][c]:
            break
    score *= visible_trees

    return score

max_scenic_score = -1
for (r, _) in enumerate(grid):
    for (c, _) in enumerate(grid[0]):
        ss = scenic_score(r, c)
        if ss > max_scenic_score:
            max_scenic_score = ss

print(max_scenic_score)
