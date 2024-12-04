from collections import Counter

# Part 1
a, b = [], []

with open("inputs/01") as f:
    for line in f.readlines():
        x, y = map(int, line.split())
        a.append(x)
        b.append(y)


tot = 0
for i, j in zip(sorted(a), sorted(b)):
    tot += abs(i - j)
print(f"Part 1: {tot}")

# Part 2
counter_b = Counter(b)
tot = 0

for i in a:
    tot += i * counter_b[i]
print(f"Part 2: {tot}")
