mapper = {'X': 'A', 'Y': 'B', 'Z': 'C'}
points = {'A': 1, 'B': 2, 'C': 3}
winnings = {'B': 'A', 'C': 'B', 'A': 'C'}
inv_winnings = {v: k for k, v in winnings.items()}

score_1, score_2 = 0, 0

with open('inputs/02') as f:
    for line in f.readlines():
        shape_a, b = line.split()
        shape_b = mapper[b]

        # part 1
        score_1 += points[shape_b]
        if shape_a == shape_b:
            score_1 += 3
        elif winnings[shape_b] == shape_a:
            score_1 += 6

        # part 2
        if b == 'X':
            score_2 += points[winnings[shape_a]]
        elif b == 'Y':
            score_2 += points[shape_a]
            score_2 += 3
        elif b == 'Z':
            score_2 += points[inv_winnings[shape_a]]
            score_2 += 6

print(f'Part 1: {score_1}')
print(f'Part 2: {score_2}')
