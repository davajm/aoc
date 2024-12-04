# Part 1
report = []
with open("inputs/02") as f:
    report = [[int(x) for x in line.split()] for line in f.readlines()]

tot = 0
for levels in report:
    ascending = True if levels[1] > levels[0] else False
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i - 1])
        if (
            (ascending and levels[i] < levels[i - 1])
            or (not ascending and levels[i] > levels[i - 1])
            or diff < 1
            or diff > 3
        ):
            break
    else:
        tot += 1

print(f"Part 1: {tot}")

# Part 2
tot = 0
for prev_levels in report:
    new_levels = [prev_levels]
    for i in range(len(prev_levels)):
        new_levels.append(prev_levels[0:i] + prev_levels[i + 1 :])
    for levels in new_levels:
        ascending = True if levels[1] > levels[0] else False
        for i in range(1, len(levels)):
            diff = abs(levels[i] - levels[i - 1])
            if (
                (ascending and levels[i] < levels[i - 1])
                or (not ascending and levels[i] > levels[i - 1])
                or diff < 1
                or diff > 3
            ):
                break
        else:
            tot += 1
            break
print(f"Part 2: {tot}")
