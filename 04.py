def format_line(line):
    line = line.rstrip('\n').split(',')
    line = [tuple(int(x) for x in interval.split('-')) for interval in line]
    return line

with open('inputs/04') as f:
    lines = [format_line(line) for line in f.readlines()]

contains, overlaps = 0, 0
for line in lines:
    a, b = line
    # part 1
    if a[0] >= b[0] and a[1] <= b[1]:
        contains +=1
    elif b[0] >= a[0] and b[1] <= a[1]:
        contains += 1
    # part 2
    if b[0] <= a[1] and b[1] >= a[0]:
        overlaps += 1
    elif a[0] <= b[1] and a[1] >= b[0]:
        overlaps += 1
print(f'Part 1: {contains}')
print(f'Part 2: {overlaps}')
