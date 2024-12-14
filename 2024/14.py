inputs = []
with open("inputs/14") as f:
    for line in f.readlines():
        pos, vel = line.strip().split()
        x, y = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        inputs.append([x, y, vx, vy])

GRID_SIZE = (101, 103)


def move(robots):
    for idx, (x, y, vx, vy) in enumerate(robots):
        x += vx
        y += vy
        if x >= GRID_SIZE[0]:
            x -= GRID_SIZE[0]
        if x < 0:
            x += GRID_SIZE[0]
        if y < 0:
            y += GRID_SIZE[1]
        if y >= GRID_SIZE[1]:
            y -= GRID_SIZE[1]
        robots[idx] = [x, y, vx, vy]
    return robots


# Part 1
robots = inputs.copy()
for _ in range(100):
    robots = move(robots)

quad_count = [0, 0, 0, 0]
for inp in robots:
    if inp[0] < GRID_SIZE[0] // 2 and inp[1] < GRID_SIZE[1] // 2:
        quad_count[0] += 1
    elif inp[0] < GRID_SIZE[0] // 2 and inp[1] > GRID_SIZE[1] // 2:
        quad_count[1] += 1
    elif inp[0] > GRID_SIZE[0] // 2 and inp[1] < GRID_SIZE[1] // 2:
        quad_count[2] += 1
    elif inp[0] > GRID_SIZE[0] // 2 and inp[1] > GRID_SIZE[1] // 2:
        quad_count[3] += 1

tot = quad_count[0]
for x in quad_count[1:]:
    tot *= x
print(f"Part 1: {tot}")

# Part 2, find tree...
robots = inputs.copy()
for i in range(100000):
    robots = move(robots)
    grid = [["."] * GRID_SIZE[0] for _ in range(GRID_SIZE[1])]
    for inp in robots:
        grid[inp[1]][inp[0]] = "#"

    # Cols with at least 8 consecutive #
    counter_col = [0] * GRID_SIZE[0]
    can_be_tree = False
    for y in range(GRID_SIZE[1]):
        for x in range(GRID_SIZE[0]):
            if y > 0 and grid[y][x] == "#" and grid[y - 1][x] == "#":
                counter_col[x] += 1
                if counter_col[x] >= 9:
                    can_be_tree = True
                    break
            else:
                counter_col[x] = 0
        if can_be_tree:
            break

    if can_be_tree:
        print(f"Iteration: {i+1}")
        for line in grid:
            print("".join(line))
        input()
