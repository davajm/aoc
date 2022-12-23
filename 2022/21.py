with open("inputs/21") as f:
    instructions = [line.rstrip("\n").split(" ") for line in f.readlines()]

# part 1
def get_mapper():
    mapper = {}
    for instruction in instructions:
        a = instruction[0][:-1]
        if len(instruction) == 2:
            mapper[a] = int(instruction[1])
        else:
            mapper[a] = tuple(instruction[1:])
            if a == "root":
                root = instruction[1:]
    return mapper, root


def compute(a):
    if isinstance(mapper[a], (int, float)):
        return mapper[a]

    x, op, y = mapper[a]

    if op == "+":
        mapper[a] = compute(x) + compute(y)
    elif op == "-":
        mapper[a] = compute(x) - compute(y)
    elif op == "/":
        mapper[a] = compute(x) / compute(y)
    elif op == "*":
        mapper[a] = compute(x) * compute(y)
    return mapper[a]


mapper, _ = get_mapper()
x = int(compute("root"))
print(f"Part 1: {x}")

# part 2
mapper, root = get_mapper()
rev_mapper = {}
rev_op = {"+": "-", "-": "+", "/": "*", "*": "/"}
for instruction in instructions:
    if len(instruction) == 4:
        a, b, op, c = instruction
        a = a[:-1]
        rev_mapper[b] = (a, rev_op[op], c, True)

        if op in ["-", "/"]:
            rev_mapper[c] = (b, op, a, False)
        else:
            rev_mapper[c] = (a, rev_op[op], b, True)

del mapper["humn"]
try:
    x = compute(root[0])
    mapper[root[2]] = x
except:
    x = compute(root[2])
    mapper[root[0]] = x


def compute_rev(a):
    if a in mapper and isinstance(mapper[a], (int, float)):
        return mapper[a]

    x, op, y, dir = rev_mapper[a]

    if op == "+":
        mapper[a] = compute_rev(x) + compute(y) if dir else compute(x) + compute_rev(y)
    elif op == "-":
        mapper[a] = compute_rev(x) - compute(y) if dir else compute(x) - compute_rev(y)
    elif op == "/":
        mapper[a] = compute_rev(x) / compute(y) if dir else compute(x) / compute_rev(y)
    elif op == "*":
        mapper[a] = compute_rev(x) * compute(y) if dir else compute(x) * compute_rev(y)
    return mapper[a]


x = int(compute_rev("humn"))
print(f"Part 2: {x}")
