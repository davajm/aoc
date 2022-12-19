with open("inputs/17") as f:
    moves = f.readline().rstrip('\n')


shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]
widths = [4, 3, 3, 1, 2]

chamber = {(0, i) for i in range(7)}
shape_ind, move_ind = 0, 0
max_y, x, y = 0, 2, 4
rocks = 0
down = False

while rocks < 2022:
    next_x, next_y = x, y
    if down:
        next_y -= 1
        down = False
    else:
        if moves[move_ind] == '>':
            if x+widths[shape_ind] < 7:
                next_x += 1
        elif x > 0:
            next_x -= 1
        move_ind = (move_ind+1)%len(moves)
        down = True

    # rest/collision check
    for point in shapes[shape_ind]:
        if (point[0]+next_y, point[1]+next_x) in chamber:
            if not down:
                for point in shapes[shape_ind]:
                    max_y = max(max_y, point[0]+y)
                    chamber.add((point[0]+y, point[1]+x))
                shape_ind = (shape_ind+1)%5
                x, y = 2, max_y+4
                rocks += 1
            break
    else:
        x, y = next_x, next_y
 
print(f'Part 1: {max_y}')
