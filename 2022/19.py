blueprints = []
with open("inputs/19") as f:
    lines = f.read().replace('\n', '').split('Each ')[1:]

for i in range(0, len(lines), 4):
    ore = (int(lines[i].split('costs ')[1].split(' ore')[0]), 0, 0)
    clay = (int(lines[i+1].split('costs ')[1].split(' ore')[0]), 0, 0)
    obsidian = lines[i+2].split('costs ')[1].split(' ore ')
    obsidian = (int(obsidian[0]), int(obsidian[1].split(' ')[1]), 0)
    geode = lines[i+3].split('costs ')[1].split(' ore ')
    geode = (int(geode[0]), 0, int(geode[1].split(' ')[1]), 0)
    blueprints.append((ore, clay, obsidian, geode))


def search(blueprint, ore, clay, obs, geo, r1, r2, r3, r4, time):
    id = (ore, clay, obs, geo, r1, r2, r3, r4, time)
    if time == 0:
        return geo

    if id in memoize:
        return memoize[id]

    geos = []
    geos.append(search(blueprint, ore+r1, clay+r2, obs+r3, geo+r4, r1, r2, r3, r4, time-1))

    if ore >= blueprint[0][0]:
        geos.append(search(blueprint, ore+r1-blueprint[0][0], clay+r2, obs+r3, geo+r4, r1+1, r2, r3, r4, time-1))
    if ore >= blueprint[1][0]:
        geos.append(search(blueprint, ore+r1-blueprint[1][0], clay+r2, obs+r3, geo+r4, r1, r2+1, r3, r4, time-1))
    if ore >= blueprint[2][0] and clay >= blueprint[2][1]:
        geos.append(search(blueprint, ore+r1-blueprint[2][0], clay+r2-blueprint[2][1], obs+r3, geo+r4, r1, r2, r3+1, r4, time-1))
    if ore >= blueprint[3][0] and obs >= blueprint[3][2]:
        geos.append(search(blueprint, ore+r1-blueprint[3][0], clay+r2, obs+r3-blueprint[3][2], geo+r4, r1, r2, r3, r4+1, time-1))

    memoize[id] = max(geos)
    return max(geos)

geos = []
for blueprint in blueprints:
    memoize = {}
    geos.append(search(blueprint, 0, 0, 0, 0, 1, 0, 0, 0, 24))

quality = sum([geo*(i+1) for i, geo in enumerate(geos)])
print(f'Part 1: {quality}')
