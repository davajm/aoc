def move_piece(first, second):
    dx, dy = first[0] - second[0], first[1] - second[1]

    if abs(dx) >= 2 and abs(dy) == 0:
        if dx >= 1:
            second = first[0] - 1, second[1]
        else:
            second = first[0] + 1, second[1]
    elif abs(dy) >= 2 and abs(dx) == 0:
        if dy >= 1:
            second = second[0], first[1] - 1
        else:
            second = second[0], first[1] + 1
    elif abs(dx) >= 2 or abs(dy) >= 2:
        second = second[0] + dx // abs(dx), second[1] + dy // abs(dy)
    return second


with open("inputs/09") as f:
    moves = [line.rstrip("\n").split() for line in f.readlines()]

head = (0, 0)
tail = (0, 0)
rest = [(0, 0)] * 8
visited = {(0, 0)}
visited_2 = {(0, 0)}

for dir, steps in moves:
    x, y = head
    for step in range(int(steps)):
        if dir == "U":
            y += 1
        elif dir == "D":
            y -= 1
        elif dir == "L":
            x -= 1
        elif dir == "R":
            x += 1
        head = (x, y)

        # part 1
        tail = move_piece(head, tail)
        visited.add(tail)

        # part 2
        start = tail
        for i in range(len(rest)):
            rest[i] = move_piece(start, rest[i])
            start = rest[i]
        visited_2.add(rest[-1])

print(f"Part 1: {len(visited)}")
print(f"Part 2: {len(visited_2)}")
