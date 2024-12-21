grid = []
with open("inputs/20") as f:
    i = 0
    for line in f.readlines():
        grid_line = []
        for j in range(len(line.strip())):
            grid_line.append(line[j])
            if line[j] == "S":
                start = (i, j)
            elif line[j] == "E":
                end = (i, j)
        grid.append(grid_line)
        i += 1

# Create path
path = [start]
x, y = start
while (x, y) != end:
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for x2, y2 in neighbors:
        if (
            0 <= x2 < len(grid)
            and 0 <= y2 < len(grid[0])
            and grid[x2][y2] != "#"
            and (x2, y2) not in path
        ):
            path.append((x2, y2))
            x, y = x2, y2
            break

# Cheat
tot_1, tot_2 = 0, 0
for i in range(len(path)):
    for j in range(i + 1, len(path)):
        dist = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
        saved = j - i - dist
        if saved >= 100:
            if dist <= 20:
                tot_2 += 1
            if dist == 2:
                tot_1 += 1

print(f"Part 1: {tot_1}")
print(f"Part 2: {tot_2}")
