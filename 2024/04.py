# Part 1
with open("inputs/04") as f:
    grid = [[x for x in line.rstrip("\n")] for line in f.readlines()]

queue = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "X":
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    queue.append((i, j, di, dj, "X"))

tot = 0
while queue:
    x, y, dx, dy, c = queue.pop()
    next_x, next_y = x + dx, y + dy
    if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[next_x]):
        continue
    next_c = grid[next_x][next_y]
    if (c == "X" and next_c == "M") or c == "M" and next_c == "A":
        queue.append((next_x, next_y, dx, dy, next_c))
    elif c == "A" and next_c == "S":
        tot += 1

print(f"Part 1: {tot}")

tot = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        x = grid[i][j]
        if x == "A" and i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[i]) - 1:
            words = []
            a = grid[i - 1][j - 1]
            b = grid[i + 1][j - 1]
            c = grid[i - 1][j + 1]
            d = grid[i + 1][j + 1]
            words.append(a + x + d)
            words.append(b + x + c)
            words.append(c + x + b)
            words.append(d + x + a)
            if words.count("MAS") == 2:
                tot += 1

print(f"Part 2: {tot}")
