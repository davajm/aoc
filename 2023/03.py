def get_adjacent(grid, i, j):
    queue = []
    if i > 0:
        queue.append((i - 1, j))
        if j > 0:
            queue.append((i - 1, j - 1))
        if j < len(grid[i]) - 1:
            queue.append((i - 1, j + 1))
    if i < len(grid) - 1:
        queue.append((i + 1, j))
        if j > 0:
            queue.append((i + 1, j - 1))
        if j < len(grid[i]) - 1:
            queue.append((i + 1, j + 1))
    if j > 0:
        queue.append((i, j - 1))
    if j < len(grid[i]) - 1:
        queue.append((i, j + 1))

    return queue


def part_check(grid, i, j):
    queue = get_adjacent(grid, i, j)

    for x, y in queue:
        if not grid[x][y].isdigit() and grid[x][y] != ".":
            return True
    return False


def gear_check(grid, i, j):
    queue = get_adjacent(grid, i, j)
    return {(x, y) for x, y in queue if grid[x][y] == "*"}


with open("inputs/03") as f:
    grid = [[x for x in line.rstrip("\n")] for line in f.readlines()]

tot = 0
gears = {}
number, part, gear_parts = [], False, set()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        c = grid[i][j]
        if c.isdigit():
            number.append(c)
            part = part or part_check(grid, i, j)
            gear_parts |= gear_check(grid, i, j)
            if j == len(grid[i]) - 1:
                tot += int("".join(number)) if number and part else 0
                for gp in gear_parts:
                    if gp not in gears:
                        gears[gp] = [int("".join(number))]
                    else:
                        gears[gp].append(int("".join(number)))
                number, part, gear_parts = [], False, set()
        else:
            tot += int("".join(number)) if number and part else 0
            for gp in gear_parts:
                if gp not in gears:
                    gears[gp] = [int("".join(number))]
                else:
                    gears[gp].append(int("".join(number)))
            number, part, gear_parts = [], False, set()
print(f"Part 1: {tot}")

tot_2 = 0
for k in gears:
    if len(gears[k]) == 2:
        tot_2 += gears[k][0] * gears[k][1]
print(f"Part 2: {tot_2}")
