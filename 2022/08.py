def get_score(val, prev):
    i = 0
    while val > prev[-i - 1] and i < len(prev) - 1:
        i += 1
    return i + 1


with open("inputs/08") as f:
    grid = [[int(x) for x in line.rstrip("\n")] for line in f.readlines()]

visible = [
    [
        True if row in [0, len(grid) - 1] or col in [0, len(grid[row]) - 1] else False
        for col in range(len(grid[row]))
    ]
    for row in range(len(grid))
]
scores = [[[0, 0, 0, 0] for _ in range(len(row))] for row in grid]

for row in range(len(grid)):
    max_l, max_r = grid[row][0], grid[row][-1]
    prev_l, prev_r = [max_l], [max_r]
    for col in range(1, len(grid[row])):
        val_l, val_r = grid[row][col], grid[row][-col - 1]
        # part 1
        if val_l > max_l:
            visible[row][col] = True
            max_l = val_l
        if val_r > max_r:
            visible[row][-col - 1] = True
            max_r = val_r
        # part 2
        scores[row][col][0] = get_score(val_l, prev_l)
        scores[row][-col - 1][1] = get_score(val_r, prev_r)
        prev_l.append(val_l)
        prev_r.append(val_r)

for col in range(len(grid[0])):
    max_t, max_b = grid[0][col], grid[-1][col]
    prev_t, prev_b = [max_t], [max_b]
    for row in range(1, len(grid)):
        val_t, val_b = grid[row][col], grid[-row - 1][col]
        # part 1
        if grid[row][col] > max_t:
            visible[row][col] = True
            max_t = val_t
        if grid[-row - 1][col] > max_b:
            visible[-row - 1][col] = True
            max_b = val_b
        # part 2
        scores[row][col][2] = get_score(val_t, prev_t)
        scores[-row - 1][col][3] = get_score(val_b, prev_b)
        prev_t.append(val_t)
        prev_b.append(val_b)

# part 2
best_score = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        l, r, t, b = scores[row][col]
        best_score = max(best_score, l * r * t * b)

print(f"Part 1: {sum(map(sum, visible))}")
print(f"Part 2: {best_score}")
