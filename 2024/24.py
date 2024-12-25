from collections import deque

vars = {}
queue = deque()
with open("inputs/24") as f:
    line = f.readline().strip()
    while line != "":
        a, b = line.split(": ")
        vars[a] = int(b)
        line = f.readline().strip()

    line = f.readline().strip()
    while line != "":
        a, op, b, _, c = line.split(" ")
        queue.append((a, op, b, c))
        line = f.readline().strip()

while queue:
    a, op, b, c = queue.popleft()
    if a not in vars or b not in vars:
        queue.append((a, op, b, c))
        continue
    if op == "AND":
        vars[c] = vars[a] & vars[b]
    elif op == "OR":
        vars[c] = vars[a] | vars[b]
    elif op == "XOR":
        vars[c] = vars[a] ^ vars[b]

# Part 1
i = 0
tot = []
while f"z{i:02}" in vars:
    tot.append(vars[f"z{i:02}"])
    i += 1

print(f"Part 1: {int(''.join(map(str, tot[::-1])), 2)}")
