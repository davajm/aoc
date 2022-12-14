def get_grid(line_points):
    # generate grid using input
    grid = [["." for _ in range(min_x, max_x + 1)] for _ in range(max_y + 1)]
    grid[0][500 - min_x] = "+"

    for line in line_points:
        x, y = line[0]
        grid[y][x - min_x] = "#"
        for point in line[1:]:
            for i in range(min(x, point[0]), max(x, point[0]) + 1):
                grid[y][i - min_x] = "#"
            for i in range(min(y, point[1]), max(y, point[1]) + 1):
                grid[i][x - min_x] = "#"
            x, y = point
    return grid


# parse input
line_points = []
min_x, max_x, max_y = None, 0, 0
with open("inputs/14") as f:
    for line in f.readlines():
        points = []
        for point in line.split(" -> "):
            x, y = map(int, point.split(","))
            min_x = min(min_x, x) if min_x else x
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            points.append((x, y))
        line_points.append(points)

grid = get_grid(line_points)

# part 1
total, done = 0, False
while not done:
    x, y = 500 - min_x, 0
    while y < len(grid) - 1 and x >= 0 and x < len(grid[0]) - 1:
        if grid[y + 1][x] == ".":
            y += 1
        elif grid[y + 1][x - 1] == ".":
            x -= 1
            y += 1
        elif grid[y + 1][x + 1] == ".":
            x += 1
            y += 1
        else:
            if grid[y][x] != "o":
                total += 1
                grid[y][x] = "o"
            break
    else:
        done = True

# for line in grid:
#    print(''.join(line))
print(f"Part 1: {total}")

# add floor for part 2
grid = get_grid(line_points)
grid.append(["." for _ in range(len(grid[0]))])
grid.append(["#" for _ in range(len(grid[0]))])
total, done = 0, False

while not done:
    x, y = 500 - min_x, 0
    while y < len(grid) - 1:
        if x == 0:
            for i in range(len(grid)):
                grid[i].insert(0, ".")
            grid[-1][0] = "#"
            min_x -= 1
            x -= 1
        if x == len(grid[0]) - 1:
            for i in range(len(grid)):
                grid[i].append(".")
            grid[-1][-1] = "#"
        if grid[y + 1][x] == ".":
            y += 1
        elif grid[y + 1][x - 1] == ".":
            x -= 1
            y += 1
        elif grid[y + 1][x + 1] == ".":
            x += 1
            y += 1
        else:
            if grid[y][x] != "o":
                total += 1
                grid[y][x] = "o"
            if y == 0:
                done = True
            break

# for line in grid:
#    print(''.join(line))
print(f"Part 2: {total}")
