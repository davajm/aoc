# parse input
beacons = set()
sensors = {}
with open("inputs/15") as f:
    for line in f.readlines():
        line = line.rstrip("\n").split(" ")
        sx, sy = int(line[2][2:-1]), int(line[3][2:-1])
        bx, by = int(line[-2][2:-1]), int(line[-1][2:])

        sensors[(sx, sy)] = (bx, by)
        beacons.add((bx, by))

# part 1
covered = set()
target = 2000000

for sensor in sensors:
    sx, sy = sensor
    bx, by = sensors[sensor]
    max_diff, diff = abs(sx - bx) + abs(sy - by), abs(sy - target)
    x1, x2 = sx, sx

    while diff <= max_diff:
        if (x1, target) not in beacons:
            covered.add(x1)
        if (x2, target) not in beacons:
            covered.add(x2)
        x1 -= 1
        x2 += 1
        diff += 1
print(f"Part 1: {len(covered)}")

# part 2
# very slow.. probably should optimize at some point
max_pos = 4000000
potential_points = set()
for sensor in sensors:
    sx, sy = sensor
    bx, by = sensors[sensor]
    diff = abs(sx - bx) + abs(sy - by) + 1

    y = sy
    for i in range(diff):
        if sy - i >= 0 and sy - i <= max_pos:
            if sx - diff + i >= 0 and sx - diff + i <= max_pos:
                potential_points.add((sx - diff + i, sy - i))
            if sx + diff - i >= 0 and sx + diff - i <= max_pos:
                potential_points.add((sx + diff - i, sy - i))
        if sy + i >= 0 and sy + i <= max_pos:
            if sx - diff + i >= 0 and sx - diff + i <= max_pos:
                potential_points.add((sx - diff + i, sy + i))
            if sx + diff - i >= 0 and sx + diff - i <= max_pos:
                potential_points.add((sx + diff - i, sy + i))

for point in potential_points:
    px, py = point
    for sensor in sensors:
        sx, sy = sensor
        bx, by = sensors[sensor]
        max_diff = abs(sx - bx) + abs(sy - by)
        diff = abs(px - sx) + abs(py - sy)
        if diff <= max_diff:
            break
    else:
        print(f"Part 2: {px*4000000+py}")
        break
