mappers = []
with open("inputs/05") as f:
    seeds = [int(x) for x in f.readline().rstrip("\n").split(": ")[1].split()]
    mapper = []
    for line in f.readlines():
        line = line.rstrip("\n")
        if "map" in line:
            if mapper:
                mappers.append(mapper)
            mapper = []
        elif line:
            mapper.append(tuple(map(int, line.split())))
    mappers.append(mapper)

for mapper in mappers:
    new_seeds = {}
    for seed in seeds:
        for m in mapper:
            if seed >= m[1] and seed <= m[1] + m[2]:
                new_seeds[seed] = m[0] + (seed - m[1])
    seeds = [new_seeds[x] if x in new_seeds else x for x in seeds]
print(f"Part 1: {min(seeds)}")


def get_new_seed(a, b, pos):
    if a[1] < b[0] or a[0] > b[1]:
        return None

    start = max(a[0], b[0])
    end = min(a[1], b[1])
    shift = pos - b[0]
    new_ranges = []

    if a[0] < start:
        new_ranges.append((a[0], start - 1))

    if a[1] > end:
        new_ranges.append((end + 1, a[1]))

    return ((start + shift, end + shift), new_ranges)


mappers = []
with open("inputs/05") as f:
    seeds = [int(x) for x in f.readline().rstrip("\n").split(": ")[1].split()]
    seeds = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    mapper = []
    for line in f.readlines():
        line = line.rstrip("\n")
        if "map" in line:
            if mapper:
                mappers.append(mapper)
            mapper = []
        elif line:
            mapper.append(tuple(map(int, line.split())))
    mappers.append(mapper)

for mapper in mappers:
    modified = []
    for m in mapper:
        i = len(seeds) - 1
        while i >= 0:
            seed = seeds[i]
            new_seed = get_new_seed(seed, (m[1], m[1] + m[2] - 1), m[0])
            if new_seed:
                modified.append(new_seed[0])
                seeds.pop(i)
                seeds.extend(new_seed[1])
            i -= 1
    seeds.extend(modified)
    modified = []

print(f"Part 2: {min([x[0] for x in seeds])}")
