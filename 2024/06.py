with open("inputs/06") as f:
    grid = [[x for x in line.rstrip("\n")] for line in f.readlines()]


# Find starting pos
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in ["v", "^", "<", ">"]:
            start = (i, j, grid[i][j])

# Map directions to movement and next direction
mapper = {"^": (-1, 0, ">"), ">": (0, 1, "v"), "v": (1, 0, "<"), "<": (0, -1, "^")}

# Part 1
x, y, dir = start
visited = set()
while x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]):
    a, b, c = mapper[dir]
    if grid[x][y] == "#":
        x -= a
        y -= b
        dir = c
    else:
        visited.add((x, y))
        x += a
        y += b

print(f"Part 1: {len(visited)}")

# Part 2, brute force, takes a couple of seconds
tot = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            obstacle = (i, j)
            x, y, dir = start
            visited_with_dir = set()
            while x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]):
                a, b, c = mapper[dir]
                if grid[x][y] == "#" or (x, y) == obstacle:
                    x -= a
                    y -= b
                    dir = c
                else:
                    if (x, y, dir) in visited_with_dir:
                        tot += 1
                        break
                    visited_with_dir.add((x, y, dir))
                    x += a
                    y += b

print(f"Part 2: {tot}")
