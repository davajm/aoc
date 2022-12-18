from collections import deque

with open("inputs/18") as f:
    cubes = [tuple(map(int, line.rstrip("\n").split(","))) for line in f.readlines()]

# part 1
grid = set()
sides = 0
for x, y, z in cubes:
    sides += 6
    for i in [-1, 1]:
        if (x + i, y, z) in grid:
            sides -= 2
        if (x, y + i, z) in grid:
            sides -= 2
        if (x, y, z + i) in grid:
            sides -= 2
    grid.add((x, y, z))

print(f"Part 1: {sides}")

# part 2
min_x, min_y, min_z = cubes[0]
max_x, max_y, max_z = cubes[0]

for x, y, z in cubes:
    min_x, min_y, min_z = min(min_x, x), min(min_y, y), min(min_z, z)
    max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)

# increase "bounding box" by 1
min_x, min_y, min_z = (x - 1 for x in (min_x, min_y, min_z))
max_x, max_y, max_z = (x + 1 for x in (max_x, max_y, max_z))

queue = deque([(min_x, min_y, min_z)])

visited, total = set(), 0
while queue:
    x, y, z = queue.popleft()
    if (x, y, z) in visited:
        continue
    visited.add((x, y, z))
    if x < min_x or y < min_y or z < min_z:
        continue
    if x > max_x or y > max_y or z > max_z:
        continue

    for i in [-1, 1]:
        if (x + i, y, z) in grid:
            total += 1
        elif (x + i, y, z) not in visited:
            queue.append((x + i, y, z))
        if (x, y + i, z) in grid:
            total += 1
        elif (x, y + i, z) not in visited:
            queue.append((x, y + i, z))
        if (x, y, z + i) in grid:
            total += 1
        elif (x, y, z + i) not in visited:
            queue.append((x, y, z + i))
print(f"Part 2: {total}")
