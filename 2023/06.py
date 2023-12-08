mappers = []
with open("inputs/06") as f:
    lines = [line.rstrip("\n").split(": ")[1].split() for line in f.readlines()]

# Part 1
races = [(int(lines[0][i]), int(lines[1][i])) for i in range(len(lines[0]))]
tot = 1
for duration, record in races:
    ways = 0
    for i in range(duration + 1):
        attempt = (duration - i) * i

        if attempt > record:
            ways += 1
    tot *= ways
print(f"Part 1: {tot}")

# Part 2
duration = int("".join(lines[0]))
record = int("".join(lines[1]))
ways = 0
for i in range(duration + 1):
    attempt = (duration - i) * i
    if attempt > record:
        ways += 1
print(f"Part 2: {ways}")
