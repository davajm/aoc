grid, moves = [], []
with open("inputs/15") as f:
    line = f.readline().rstrip("\n")
    while line != "":
        grid.append(list(line))
        line = f.readline().rstrip("\n")

    for line in f.readlines():
        for move in line.rstrip("\n"):
            moves.append(move)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            robot = (int(i), int(j))

# Wide grid for part 2
wide_grid = []
for row in grid:
    new_row = []
    for cell in row:
        if cell == "O":
            new_row.extend("[]")
        elif cell == "@":
            new_row.extend(cell + ".")
        else:
            new_row.extend(cell * 2)
    wide_grid.append(new_row)

steps = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

# Part 1
def move1(x, y, dir):
    tx = x + steps[dir][0]
    ty = y + steps[dir][1]

    if tx < 0 or tx >= len(grid) or ty < 0 or ty >= len(grid[0]) or grid[tx][ty] == "#":
        return (x, y)

    # Box in the way, attempt to move it first
    if grid[tx][ty] == 'O':
        move1(tx, ty, dir)

    if grid[tx][ty] == ".":
        grid[tx][ty] = grid[x][y]
        grid[x][y] = "."
        return (tx, ty)

    return (x, y)

x, y = robot
for dir in moves:
    x, y = move1(x, y, dir)

tot = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            tot += i * 100 + j
print(f"Part 1: {tot}")


# Part 2 (ugly!)
def move2(x, y, dir):

    # Helper, first pass to check if robot can move
    def moveable(x, y, dir):
        tx = x + steps[dir][0]
        ty = y + steps[dir][1]
        if tx < 0 or tx >= len(wide_grid) or ty < 0 or ty >= len(wide_grid[0]) or wide_grid[tx][ty] == "#":
            return False
        if wide_grid[tx][ty] == '.':
            return True
        if dir in ["<", ">"]:
            return moveable(tx, ty, dir)
        if wide_grid[tx][ty] == '[':
            return moveable(tx, ty, dir) and moveable(tx, ty+1, dir)
        if wide_grid[tx][ty] ==']':
            return moveable(tx, ty, dir) and moveable(tx, ty-1, dir)
        return False
    
    # Helper, second pass to move robot
    def move(x, y, dir):
        tx = x + steps[dir][0]
        ty = y + steps[dir][1]

        if tx < 0 or tx >= len(wide_grid) or ty < 0 or ty >= len(wide_grid[0]) or wide_grid[tx][ty] == "#":
            return (x, y)
        
        if dir in ['^', 'v']:
            if wide_grid[tx][ty] == ']':
                move(tx, ty-1, dir)
            elif wide_grid[tx][ty] == '[':
                move(tx, ty+1, dir)

        if wide_grid[tx][ty] != '.':
            move(tx, ty, dir)
        tmp = wide_grid[tx][ty]
        wide_grid[tx][ty] = wide_grid[x][y]
        wide_grid[x][y] = tmp

        return (tx, ty)

    if moveable(x, y, dir):        
        return move(x, y, dir)
    return (x, y)

x, y = robot
y *= 2
for dir in moves:
    x, y, = move2(x, y, dir)

tot = 0
for i in range(len(wide_grid)):
    for j in range(len(wide_grid[i])):
        if wide_grid[i][j] == "[":
            tot += i * 100 + j
print(f"Part 2: {tot}")