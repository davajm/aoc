# Part 1
tot = 0
with open("inputs/01") as f:
    for line in f.readlines():
        first, last = None, None
        for c in line:
            if c.isdigit():
                if not first:
                    first = c
                last = c
        tot += int(first + last)
print(f"Part 1: {tot}")

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Part 2
tot = 0
with open("inputs/01") as f:
    for line in f.readlines():
        first, i = None, 0
        while not first:
            if line[i].isdigit():
                first = line[i]
            for j in range(i):
                if line[j:i] in numbers:
                    first = numbers[line[j:i]]
            i += 1

        last, i = None, len(line) - 1
        while not last:
            if line[i].isdigit():
                last = line[i]
            for j in range(len(line) - 1, i, -1):
                if line[i:j] in numbers:
                    last = numbers[line[i:j]]
            i -= 1
        tot += int(first + last)
print(f"Part 2: {tot}")
