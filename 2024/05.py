# Part 1 & 2
rules = {}
with open("inputs/05") as f:
    line = f.readline().rstrip("\n")
    while line != "":
        a, b = map(int, line.split("|"))
        if a in rules:
            rules[a].add(b)
        else:
            rules[a] = {b}
        line = f.readline().rstrip("\n")

    instructions = [list(map(int, line.rstrip().split(","))) for line in f.readlines()]
    tot_1, tot_2 = 0, 0
    for instruction in instructions:
        instruction_pos = []
        for i in instruction:
            pos = 0
            for j in instruction:
                if j in rules[i]:
                    pos += 1
            instruction_pos.append((i, pos))
        instruction_pos.sort(key=lambda x: x[1], reverse=True)
        instruction_sorted = [x[0] for x in instruction_pos]

        if instruction_sorted == instruction:
            tot_1 += instruction[len(instruction) // 2]
        else:
            tot_2 += instruction_sorted[len(instruction_sorted) // 2]

print(f"Part 1: {tot_1}")
print(f"Part 2: {tot_2}")
