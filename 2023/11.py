def get_galaxies(replace=1):
    galaxies = []
    replace -= 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                new_i, new_j = i, j
                for row in empty_rows:
                    if row < i:
                        new_i += replace
                for col in empty_cols:
                    if col < j:
                        new_j += replace
                galaxies.append((new_i, new_j))
    return galaxies


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


with open("inputs/11") as f:
    grid = [[c for c in line.rstrip("\n")] for line in f.readlines()]
empty_rows = [i for i in range(len(grid)) if "#" not in grid[i]]
empty_cols = [j for j in range(len(grid[0])) if "#" not in [row[j] for row in grid]]

# Part 1
galaxies = get_galaxies(2)
tot = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        tot += distance(galaxies[i], galaxies[j])
print(f"Part 1: {tot}")

# Part 2
galaxies = get_galaxies(1000000)
tot = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        tot += distance(galaxies[i], galaxies[j])
print(f"Part 2: {tot}")
