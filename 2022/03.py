def get_priority(x):
    if x.islower():
        return ord(x) - ord('a') + 1
    return ord(x) - ord('A') + 27


with open('inputs/03') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

# part 1
sum = 0
for line in lines:
    half = len(line)//2
    first, second = set(line[:half]), set(line[half:])
    intersect = first.intersection(second).pop()
    sum += get_priority(intersect)
print(f'Part 1: {sum}')

# part 2
sum = 0
for i in range(0, len(lines), 3):
    intersect = set.intersection(*[set(line) for line in lines[i:i+3]]).pop()
    sum += get_priority(intersect)
print(f'Part 2: {sum}')
