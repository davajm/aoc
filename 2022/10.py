with open("inputs/10") as f:
    instructions = [line.rstrip("\n").split() for line in f.readlines()]

crt = [['.' for _ in range(40)] for _ in range(6)]
cycle, i, register, strength, stop = 0, 0, 1, 0, 20

while cycle < 240:
    instruction = instructions[i]
    if instruction[0] == 'noop':
        add_cycle, add_number = 1, 0
    elif instruction[0] == 'addx':
        add_cycle, add_number = 2, int(instruction[1])
    for x in range(add_cycle):
        row, col = (cycle+x)//40, (cycle+x)%40
        if col >= register-1 and col <= register+1:
            crt[row][col] = '#'  
    if cycle + add_cycle >= stop:
        strength += (stop*register)
        stop += 40
    register += add_number
    cycle += add_cycle
    i += 1

print(f'Part 1: {strength}')
print('Part 2: ')
for row in crt:
    print(''.join(row))
