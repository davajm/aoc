with open("inputs/20") as f:
    sequence = [(int(line.rstrip("\n")), False) for line in f.readlines()]

i = 0
while i < len(sequence):
    n, done = sequence[i]
    if done:
        i += 1
        continue
    del sequence[i]
    new_i = (i + n) % len(sequence)
    if new_i == 0:
        sequence.append((n, True))
    else:
        sequence.insert(new_i, (n, True))
    if new_i < i:
        i += 1

zero = sequence.index((0, True))
sum_grove = sum([sequence[(zero + i) % len(sequence)][0] for i in [1000, 2000, 3000]])
print(f"Part 1: {sum_grove}")
