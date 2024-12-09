with open("inputs/09") as f:
    disk_map = f.read()

files = []

for i in range(1, len(disk_map), 2):
    files += [str((i) // 2)] * int(disk_map[i - 1])
    files += ["."] * int(disk_map[i])
files += [str((len(disk_map)) // 2)] * int(disk_map[-1])

# Part 1
moved = files.copy()
i, j = 0, len(moved) - 1
while i < j:
    if moved[j] == ".":
        j -= 1
    elif moved[i] != ".":
        i += 1
    else:
        moved[i] = moved[j]
        moved[j] = "."
        j -= 1
        i += 1

tot = sum([i * int(moved[i]) for i in range(len(moved)) if moved[i] != "."])
print(f"Part 1: {tot}")


# Part 2 (ugly!)

moved = files.copy()
i = len(moved) - 1

while i > 0:
    if moved[i].isnumeric():
        j = i
        while i > 0 and moved[j] == moved[i - 1]:
            i -= 1

        x = 0
        while x < i:
            if moved[x] == ".":
                y = x
                while x < i and moved[y] == moved[x + 1]:
                    x += 1

                if x - y >= j - i:
                    for k in range(j - i + 1):
                        moved[y + k] = moved[j - k]
                        moved[j - k] = "."
            x += 1
    i -= 1

tot = sum([i * int(moved[i]) for i in range(len(moved)) if moved[i] != "."])
print(f"Part 2: {tot}")
