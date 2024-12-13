from collections import deque

with open("inputs/12") as f:
    grid = [[x for x in line.rstrip("\n")] for line in f.readlines()]


visited = set()
islands = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) in visited:
            continue
        queue = deque([(i, j)])
        island = set()
        while queue:
            x, y = queue.popleft()
            if (x, y) in island:
                continue
            island.add((x, y))
            for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (
                    0 <= a < len(grid)
                    and 0 <= b < len(grid[a])
                    and (a, b) not in visited
                    and grid[x][y] == grid[a][b]
                ):
                    queue.append((a, b))

        islands.append(island)
        visited.update(island)

tot = 0
for island in islands:
    perimeter = 0
    for x, y in island:
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        sides = 4
        for i, j in neighbors:
            if (i, j) in island:
                sides -= 1
        perimeter += sides
    tot += perimeter * len(island)

print(f"Part 1: {tot}")


# Part 2 (ugly!)
tot = 0
for island in islands:
    total_sides = 0
    for x, y in island:

        # Count corners
        up = (x - 1, y)
        left = (x, y - 1)
        down = (x + 1, y)
        right = (x, y + 1)

        if up not in island and left not in island:
            total_sides += 1
        if up not in island and right not in island:
            total_sides += 1
        if right not in island and down not in island:
            total_sides += 1
        if down not in island and left not in island:
            total_sides += 1

        if up in island and left in island and (x - 1, y - 1) not in island:
            total_sides += 1
        if up in island and right in island and (x - 1, y + 1) not in island:
            total_sides += 1
        if down in island and right in island and (x + 1, y + 1) not in island:
            total_sides += 1
        if down in island and left in island and (x + 1, y - 1) not in island:
            total_sides += 1

    tot += total_sides * len(island)

print(f"Part 2: {tot}")
