with open("inputs/10") as f:
    grid = [[c for c in line.rstrip("\n")] for line in f.readlines()]

starts = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
            if i > 0 and grid[i - 1][j] != ".":
                starts.append(((i - 1, j), 1))
            if i < len(grid) - 1 and grid[i + 1][j] != ".":
                starts.append(((i + 1, j), 1))
            if j > 0 and grid[i][j - 1] != ".":
                starts.append(((i, j - 1), 1))
            if j < len(grid[i]) - 1 and grid[i][j + 1] != ".":
                starts.append(((i, j + 1), 1))


def get_next_steps(pos):
    next_steps = []
    i, j = pos

    # go south
    if i < len(grid) - 1 and (
        (grid[i + 1][j] == "S")
        or (grid[i][j] in ["|", "F", "7"] and grid[i + 1][j] in ["|", "L", "J"])
    ):
        next_steps.append((i + 1, j))
    # go north
    if i > 0 and (
        (grid[i - 1][j] == "S")
        or (grid[i][j] in ["|", "L", "J"] and grid[i - 1][j] in ["|", "7", "F"])
    ):
        next_steps.append((i - 1, j))
    # go east
    if j < len(grid[i]) - 1 and (
        (grid[i][j + 1] == "S")
        or (grid[i][j] in ["-", "L", "F"] and grid[i][j + 1] in ["-", "J", "7"])
    ):
        next_steps.append((i, j + 1))
    # go west
    if j > 0 and (
        (grid[i][j - 1] == "S")
        or (grid[i][j] in ["-", "J", "7"] and grid[i][j - 1] in ["-", "L", "F"])
    ):
        next_steps.append((i, j - 1))
    return next_steps


tot = 0
loop = None
print(len(start))
for x in starts:
    visited = set()
    queue = [x]
    while queue:
        pos, farthest = queue.pop()
        for new_pos in get_next_steps(pos):
            if new_pos == start:
                if farthest + 1 > tot:
                    tot = farthest + 1
                    visited.add(start)
                    loop = visited
            elif new_pos not in visited:
                queue.append([new_pos, farthest + 1])
                visited.add(new_pos)

print(f"Part 1: {tot//2}")


# Manual inspection, S = |
grid[start[0]][start[1]] = "|"

tot = 0
for i in range(len(grid)):
    inside = False
    for j in range(len(grid[i])):
        if (i, j) in loop and grid[i][j] in {"|", "L", "J"}:
            inside = not inside
        elif inside and (i, j) not in loop:
            tot += 1
print(f"Part 2: {tot}")
