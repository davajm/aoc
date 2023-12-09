from math import lcm

mapper = {}

with open("inputs/08") as f:
    steps = f.readline().rstrip("\n")
    f.readline()

    for line in f.readlines():
        line = line.rstrip("\n")
        a, b = line.split(" = ")
        mapper[a] = b[1:-1].split(", ")

e, n = "AAA", 0
while e != "ZZZ":
    step = steps[n % len(steps)]
    e = mapper[e][0] if step == "L" else mapper[e][1]
    n += 1
print(f"Part 1: {n}")

cycles = {}
for e in mapper:
    if e[-1] == "A":
        start, n = e, 0
        while e[-1] != "Z":
            step = steps[n % len(steps)]
            e = mapper[e][0] if step == "L" else mapper[e][1]
            n += 1
        cycles[start] = n

print(f"Part 2: {lcm(*cycles.values())}")
