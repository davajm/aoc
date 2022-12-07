with open('inputs/07') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

totals = {}
stack = []
for line in lines:
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                stack.pop()
            else:
                path = f'{stack[-1]}{line[2]}/' if len(stack) > 0 else '/'
                totals[path] = 0
                stack.append(path)
    elif line[0] != 'dir':
        for dir in stack:   
            totals[dir] += int(line[0])

sum = sum(total for total in totals.values() if total <= 100000)
min = min(total for total in totals.values() if total >= (30000000-(70000000-totals['/'])))
print(f'Part 1: {sum}')
print(f'Part 2: {min}')
