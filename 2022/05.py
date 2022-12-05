from copy import deepcopy

stacks = []
moves = []
with open('inputs/05') as f:
    while True:
        line = f.readline().rstrip('\n')
        if line[1] == '1':
            f.readline()
            break
        line = [line[i+1: i + 2] for i in range(0, len(line), 4)]
        if not stacks:
            stacks = [[] for _ in range(len(line))]
        for id, crate in enumerate(line):
            if crate != ' ':
                stacks[id].append(crate)
    moves = [[int(x) for x in line.rstrip('\n').split(' ') if x.isnumeric()] for line in f.readlines()]

# part 1
crates = deepcopy(stacks)
for cnt, frm, to in moves:
    for _ in range(cnt):
        crate = crates[frm-1].pop(0)
        crates[to-1].insert(0, crate)
top_crates = ''.join(x[0] for x in crates)
print(f'Part 1: {top_crates}')

# part 2
crates = deepcopy(stacks)
for cnt, frm, to in moves:
    for i in range(cnt-1, -1, -1):
        crate = crates[frm-1].pop(i)
        crates[to-1].insert(0, crate)
top_crates = ''.join(x[0] for x in crates)
print(f'Part 2: {top_crates}')
