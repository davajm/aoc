with open("inputs/10") as f:
    grid = [[int(x) for x in line.rstrip("\n")] for line in f.readlines()]

zeros = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            zeros.append((i, j, 0))

# Part 1 & 2
queue = [(i, j, i, j, c) for i, j, c in zeros]
trails = set()
tot = 0
while queue:
    start_i, start_j, i, j, c = queue.pop()
    steps = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for x, y in steps:
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]):
            if grid[x][y] == c + 1:
                if c == 8:
                    trails.add((start_i, start_j, x, y))
                    tot += 1
                else:
                    queue.append((start_i, start_j, x, y, c + 1))

print(f"Part 1: {len(trails)}")
print(f"Part 2: {tot}")
