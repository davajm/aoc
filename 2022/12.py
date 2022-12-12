with open("inputs/12") as f:
    grid = [[x for x in line.rstrip("\n")] for line in f.readlines()]

min_path, queue, start = [], [], None
for i in range(len(grid)):
    row = []
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
            grid[i][j] = "a"
        elif grid[i][j] == "E":
            queue.append((i, j, 1))
            grid[i][j] = "z"
        row.append(None)
    min_path.append(row)

while queue:
    x, y, p = queue.pop(0)
    if not min_path[x][y]:
        min_path[x][y] = p

        if x > 0 and not min_path[x-1][y] and ord(grid[x-1][y])+1 >= ord(grid[x][y]):
            queue.append((x-1, y, p+1))
        if y > 0 and not min_path[x][y-1] and ord(grid[x][y-1])+1 >= ord(grid[x][y]):
            queue.append((x, y-1, p+1))
        if x < len(grid)-1 and not min_path[x+1][y] and ord(grid[x+1][y])+1 >= ord(grid[x][y]):
            queue.append((x+1, y, p+1))
        if y < len(grid[0])-1 and not min_path[x][y+1] and ord(grid[x][y+1])+1 >= ord(grid[x][y]):
            queue.append((x, y+1, p+1))

# part 1
shortest = min_path[start[0]][start[1]]
print(f"Part 1: {shortest-1}")

# part 2
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "a" and min_path[i][j]:
            shortest = min(shortest, min_path[i][j])
print(f"Part 2: {shortest-1}")
