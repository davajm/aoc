from functools import lru_cache

with open("inputs/19") as f:
    patterns = set(f.readline().strip().split(", "))
    f.readline()
    designs = [line.strip() for line in f.readlines()]


@lru_cache(maxsize=None)
def solve(design):
    ways = 0
    for pattern in patterns:
        if pattern == design:
            ways += 1
        elif design.startswith(pattern):
            ways += solve(design[len(pattern) :])
    return ways


tot_1, tot_2 = 0, 0
for design in designs:
    x = solve(design)
    tot_2 += x
    tot_1 += 1 if x else 0
print(f"Part 1: {tot_1}")
print(f"Part 2: {tot_2}")
