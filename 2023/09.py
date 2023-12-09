with open("inputs/09") as f:
    lines = [[int(x) for x in line.rstrip("\n").split()] for line in f.readlines()]

tot = 0
tot_2 = 0
for line in lines:
    all = [line]
    while len(set(all[-1])) != 1 or all[-1][0] != 0:
        next = []
        for i in range(len(all[-1]) - 1):
            next.append(all[-1][i + 1] - all[-1][i])
        all.append(next)

    all[-1].append(0)
    all[-1].append(0)

    for i in range(len(all) - 2, -1, -1):
        all[i].append(all[i][-1] + all[i + 1][-1])
    tot += all[0][-1]

    for i in range(len(all) - 2, -1, -1):
        all[i] = [all[i][0] - all[i + 1][0]] + all[i]

    tot_2 += all[0][0]

print(f"Part 1: {tot}")
print(f"Part 2: {tot_2}")
