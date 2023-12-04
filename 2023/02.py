tot = 0
colors = {"red": 12, "green": 13, "blue": 14}

with open("inputs/02") as f:
    i = 1
    for line in f.readlines():
        possible = True
        for set in line.rstrip().split(": ")[1].split("; "):
            for cnt_color in set.split(", "):
                x = cnt_color.split(" ")
                if x[1] not in colors or int(x[0]) > colors[x[1]]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            tot += i
        i += 1
print(f"Part 1: {tot}")


tot = 0
with open("inputs/02") as f:
    for line in f.readlines():
        colors = {}
        for set in line.rstrip().split(": ")[1].split("; "):
            for cnt_color in set.split(", "):
                x = cnt_color.split(" ")
                colors[x[1]] = max(colors.get(x[1], 0), int(x[0]))
        power = 1
        for n in colors.values():
            power *= n
        tot += power
print(f"Part 2: {tot}")
