import re

# Part 1
with open("inputs/03") as f:
    program = f.read()

muls = re.findall(r"mul\(\d+,\d+\)", program)
tot = 0
for mul in muls:
    a, b = re.findall(r"\d+", mul)
    tot += int(a) * int(b)

print(f"Part 1: {tot}")

# Part 2
muls = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", program)
tot, do = 0, True

for mul in muls:
    if mul == "do()":
        do = True
    elif mul == "don't()":
        do = False
    elif do:
        a, b = re.findall(r"\d+", mul)
        tot += int(a) * int(b)
print(f"Part 2: {tot}")
