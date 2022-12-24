with open("inputs/23") as f:
    grid = [[c for c in line.rstrip("\n")] for line in f.readlines()]


def get_elves():
    elves = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                elves.add((i, j))
    return elves


def move(dir, proposals):
    for elf in elves:
        if elf in proposals:
            continue
        i, j = elf

        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) != (0, 0):
                    if (i + x, j + y) in elves:
                        done = False
                        break
            else:
                continue
            break
        else:
            continue

        if dir == "N":
            if (
                (i - 1, j - 1) not in elves
                and (i - 1, j) not in elves
                and (i - 1, j + 1) not in elves
            ):
                proposals[elf] = (i - 1, j)
        elif dir == "S":
            if (
                (i + 1, j - 1) not in elves
                and (i + 1, j) not in elves
                and (i + 1, j + 1) not in elves
            ):
                proposals[elf] = (i + 1, j)
        elif dir == "W":
            if (
                (i - 1, j - 1) not in elves
                and (i, j - 1) not in elves
                and (i + 1, j - 1) not in elves
            ):
                proposals[elf] = (i, j - 1)
        elif dir == "E":
            if (
                (i - 1, j + 1) not in elves
                and (i, j + 1) not in elves
                and (i + 1, j + 1) not in elves
            ):
                proposals[elf] = (i, j + 1)
    return proposals


def round(elves, order):
    proposals = {}
    for dir in order:
        proposals = move(dir, proposals)

    counter = {}
    for fr, to in proposals.items():
        if to not in counter:
            counter[to] = 1
        else:
            counter[to] += 1

    new_elves = elves.copy()
    for fr, to in proposals.items():
        if counter[to] == 1:
            new_elves.remove(fr)
            new_elves.add(to)
    return new_elves


# Part 1
elves = get_elves()
order = ["N", "S", "W", "E"]
for i in range(10):
    elves = round(elves, order)
    order = order[1:] + [order[0]]

tot, first = 0, True
for elf in elves:
    y, x = elf
    if first:
        min_x, min_y, max_x, max_y = x, y, x, y
        first = False
    min_x, min_y = min(min_x, x), min(min_y, y)
    max_x, max_y = max(max_x, x), max(max_y, y)

for i in range(min_y, max_y + 1):
    for j in range(min_x, max_x + 1):
        tot += 1 if (i, j) not in elves else 0
print(f"Part 1: {tot}")

elves = get_elves()
order = ["N", "S", "W", "E"]
rounds = 0
while True:
    rounds += 1
    new_elves = round(elves, order)

    if new_elves == elves:
        break
    elves = new_elves
    order = order[1:] + [order[0]]

print(f"Part 2: {rounds}")
