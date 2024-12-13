equations = []
with open("inputs/13") as f:
    section = [f.readline().strip() for _ in range(4)]
    while any(section):
        equation = []
        for line in section[:-1]:
            a, b = line.split(": ")[1].split(", ")
            a, b = int(a[2:]), int(b[2:])
            equation.append((a, b))
        equations.append(equation)
        section = [f.readline().strip() for _ in range(4)]


def calc(a, b):
    a = (y2 * z1 - y1 * z2) / (y2 * x1 - y1 * x2)
    b = (z2 - a * x2) / y2
    if a.is_integer() and b.is_integer():
        return int(a) * 3 + int(b)
    return 0


tot_1, tot_2 = 0, 0
for equation in equations:
    x1, x2 = equation[0]
    y1, y2 = equation[1]
    z1, z2 = equation[2]

    # Part 1
    tot_1 += calc(a, b)

    # Part 2
    z1 += 10000000000000
    z2 += 10000000000000
    tot_2 += calc(a, b)


print(f"Part 1: {tot_1}")
print(f"Part 2: {tot_2}")
