with open("inputs/08") as f:
    grid = [[x for x in line.rstrip("\n")] for line in f.readlines()]

antennas = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            if grid[i][j] in antennas:
                antennas[grid[i][j]].append((i, j))
            else:
                antennas[grid[i][j]] = [(i, j)]

# Part 1
antinodes = set()
for antenna in antennas:
    for x1, y1 in antennas[antenna]:
        for x2, y2 in antennas[antenna]:
            if (x1, y1) != (x2, y2):
                new_x1, new_y1 = x1+x1-x2, y1+y1-y2
                new_x2, new_y2 = x2+x2-x1, y2+y2-y1
                if new_x1 >= 0 and new_x1 < len(grid) and new_y1 >= 0 and new_y1 < len(grid[0]):
                    antinodes.add((new_x1, new_y1))
                if new_x2 >= 0 and new_x2 < len(grid) and new_y2 >= 0 and new_y2 < len(grid[0]):
                    antinodes.add((new_x2, new_y2))
print(f"Part 1: {len(antinodes)}")

# Part 2
antinodes = set()
for antenna in antennas:
    for x1, y1 in antennas[antenna]:
        for x2, y2 in antennas[antenna]:
            if (x1, y1) != (x2, y2):
                dx, dy = x2-x1, y2-y1
                new_x, new_y = x1, y1
                while new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                    antinodes.add((new_x, new_y))
                    new_x += dx
                    new_y += dy
                
                dx, dy = x1-x2, y1-y2
                new_x, new_y = x2, y2
                while new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                    antinodes.add((new_x, new_y))
                    new_x += dx
                    new_y += dy
print(f"Part 2: {len(antinodes)}")
