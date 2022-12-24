import re

with open("inputs/22") as f:
    map = []
    max_len = 0
    line = f.readline().rstrip('\n')
    while line != '':
        line = line.rstrip('\n')
        map.append(line)
        max_len = max(max_len, len(map[-1]))
        line = f.readline().rstrip('\n')
    path = f.readline().rstrip('\n')

map = [[c for c in line.ljust(max_len, ' ')] for line in map]

dir = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '.':
            x, y = j, i
            break
    else:
        continue
    break

rot = {'R': 1, 'L': -1}
for move in re.split('(R|L)', path):
    if move in rot:
        dir = (dir+rot[move])%4
    elif move.isnumeric():
        steps = int(move)
        next_x, next_y = x, y
        while steps > 0:
            if dir in (0, 2):
                next_x += 1 if dir == 0 else -1
                if next_x < 0:
                    next_x = len(map[0]) - 1
                elif next_x >= len(map[0]):
                    next_x = 0
            elif dir in (1, 3):
                next_y += 1 if dir == 1 else -1            
                if next_y < 0:
                    next_y = len(map) - 1
                elif next_y >= len(map):
                    next_y = 0

            if map[next_y][next_x] == '#':
                break

            if map[next_y][next_x] != ' ':
                steps -= 1
                x, y = next_x, next_y
                map[y][x] = '>'

print(f'Part 1: {4*(x+1)+1000*(y+1)+dir}')
