with open("inputs/17") as f:
    registers = [int(f.readline().split(': ')[1]) for _ in range(3)]
    f.readline()
    program = [int(x) for x in f.readline().split(': ')[1].split(',')]
    opcodes = [program[i] for i in range(0, len(program), 2)]

def run_program():
    i = 0
    out = []
    while i < len(program) - 1:
        o, l = program[i], program[i+1]
        c = l if l <= 3 else registers[l-4]
        if o == 0:
            registers[0] = int(registers[0]/2**c)
        elif o == 1:
            registers[1] ^= l
        elif o == 2:
            registers[1] = c % 8
        elif o == 4:
            registers[1] ^= registers[2]
        elif o == 5:
            out.append(c%8)
        elif o == 6:
            registers[1] = int(registers[0]/2**c)
        elif o == 7:
            registers[2] = int(registers[0]/2**c)
        
        # jump
        if o == 3 and registers[0] != 0:
            i = l
        else:
            i += 2
    return out

out = run_program()
print(f"Part 1: {','.join(map(str, out))}")
