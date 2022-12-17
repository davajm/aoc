from collections import deque
import itertools


def get_valves():
    # parse inout
    valves = {}
    with open("inputs/16") as f:
        for line in f.readlines():
            line = line.rstrip("\n").split(" ")
            valve = line[1]
            rate = line[4][5:-1]
            neighbors = {tunnel.split(",")[0] for tunnel in line[9:]}
            valves[valve] = {"rate": int(rate), "neighbors": neighbors}

    return valves


valves = get_valves()

# build distance graph
for valve in valves:
    visited = {valve}
    queue = deque([(v, 1) for v in valves[valve]["neighbors"]])
    valves[valve]["distances"] = {}

    while queue:
        curr, dist = queue.popleft()
        if curr not in visited:
            visited.add(curr)
            valves[valve]["distances"][curr] = dist
            queue.extend([(nbr, dist + 1) for nbr in valves[curr]["neighbors"]])


def search(valve, time, opened):
    id = (valve, time, frozenset(sorted(opened)))
    if id in memoize:
        return memoize[id]

    total = 0
    # explore all directly or indirectly connected valves
    for neighbor in valves[valve]["distances"]:
        if neighbor not in opened:
            rate = valves[neighbor]["rate"]
            # performance improvement: only consider valves with rate > 0
            if rate > 0:
                diff_time = time - valves[valve]["distances"][neighbor] - 1
                if diff_time > 0:
                    total = max(total, rate * diff_time + search(neighbor, diff_time, opened | {valve}))

    memoize[id] = total
    return total


memoize = {}
total = search("AA", 30, set())
print(f"Part 1: {total}")

# part 2
pos_valves = {valve for valve in valves if valves[valve]["rate"] > 0}
memoize = {}

# test all combinations of opened valves
# use inversed set for elephant and find global maximum
for valve in range(len(pos_valves) + 1):
    for subset in itertools.combinations(pos_valves, valve):
        total = max(total, search("AA", 26, set(subset)) + search("AA", 26, pos_valves - set(subset)))

# quite slow
print(f"Part 2: {total}")
