from itertools import combinations

connections = {}
with open("inputs/23") as f:
    for line in f.readlines():
        a, b = line.strip().split("-")
        if a in connections:
            connections[a].add(b)
        else:
            connections[a] = {b}
        if b in connections:
            connections[b].add(a)
        else:
            connections[b] = {a}

# Part 1
seen = set()
for k in connections:
    if str(k)[0] == "t":
        neighbors = list(connections[k])
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if neighbors[i] in connections[neighbors[j]]:
                    seen.add(tuple(sorted((k, neighbors[i], neighbors[j]))))
print(f"Part 1: {len(seen)}")

# Part 2

best = set()
for k in connections:
    neighbors = connections[k]
    tot = 0
    for i in range(len(best), len(neighbors) + 1):
        for subset in combinations(neighbors, i):
            for a in subset:
                for b in subset:
                    if a != b and a not in connections[b]:
                        break  # not inter-connected
                else:
                    continue
                break
            else:
                # inter-connected
                subset += (k,)
                if len(subset) > len(best):
                    best = subset

print(f"Part 2: {','.join(sorted(best))}")
