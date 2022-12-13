def get_next(packet, i):
    # get next number or list of numbers
    # could use some cleanup...
    new_packet, brackets = [], 0
    while i < len(packet) and not (packet[i] == "," and brackets == 0):
        if packet[i] == "[":
            brackets += 1
        elif packet[i] == "]":
            brackets -= 1
            if brackets <= 0:
                if brackets == 0:
                    new_packet.append(packet[i])
                    i += 1
                break
        new_packet.append(packet[i])
        i += 1
    return "".join(new_packet), i


def compare(left, right):
    # compare two packets
    # print(f'Compare {left} vs {right}')
    if left.isnumeric() and right.isnumeric():
        a, b = int(left), int(right)
        if a < b:
            return 1
        elif b < a:
            return 2
        return None
    elif left.isnumeric():
        return compare(f"[{left}]", right)
    elif right.isnumeric():
        return compare(left, f"[{right}]")

    left_new, left_i = get_next(left, 1)
    right_new, right_i = get_next(right, 1)
    while left_new and right_new:
        comparison = compare(left_new, right_new)
        if comparison:
            return comparison
        left_new, left_i = get_next(left, left_i + 1)
        right_new, right_i = get_next(right, right_i + 1)

    if right_new and not left_new:
        return 1
    return 2 if left_new else None


with open("inputs/13") as f:
    lines = [line.rstrip("\n") for line in f.readlines() if line != "\n"]

# part 1
total, loop = 0, 1
for i in range(0, len(lines), 2):
    if compare(lines[i], lines[i + 1]) == 1:
        total += loop
    loop += 1
print(f"Part 1: {total}")

# part 2
a, b = 2, 1
for i in lines:
    if compare(i, "[[6]]") == 1:
        a += 1
    if compare(i, "[[2]]") == 1:
        b += 1
print(f"Part 2: {a*b}")
