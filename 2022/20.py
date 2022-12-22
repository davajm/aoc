with open("inputs/20") as f:
    values = [int(line.rstrip("\n")) for line in f.readlines()]


def mix(runs=1):
    for _ in range(runs):
        x = 0
        while x < len(sequence):
            for y, n in enumerate(sequence):
                if n[1] == x:
                    i = y
                    break
            n, orig = sequence[i]
            del sequence[i]
            new_i = (i + n) % len(sequence)
            if new_i == 0:
                sequence.append((n, orig))
            else:
                sequence.insert(new_i, (n, orig))
            x += 1

    zero = sequence.index((0, zero_pos))
    pos = [1000, 2000, 3000]
    return sum([sequence[(zero + x) % len(sequence)][0] for x in pos])


for i, n in enumerate(values):
    if n == 0:
        zero_pos = i

sequence = [(n, i) for i, n in enumerate(values)]
print(f"Part 1: {mix(1)}")

sequence = [(n * 811589153, i) for i, n in enumerate(values)]
print(f"Part 2: {mix(10)}")
