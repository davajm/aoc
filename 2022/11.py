import math


def parse_input():
    with open("inputs/11") as f:
        lines = [line.strip().split(': ') for line in f.readlines()]

    monkeys = []
    for i in range(0, len(lines), 7):
        section = lines[i:i+6]
        items = list(map(int, section[1][1].split(', ')))
        operation = section[2][1].split(' ')[3:]
        test = int(section[3:][0][1].split(' ')[-1])
        if_true = int(section[3:][1][1].split(' ')[-1])
        if_false = int(section[3:][2][1].split(' ')[-1])

        monkeys.append(
            {
                'items': items,
                'operation': operation,
                'test': test,
                'if_true': if_true,
                'if_false': if_false,
                'count': 0
            }
        )
    return monkeys


def monkey_in_the_middle(monkeys, rounds=20, divide=True):
    # least common multiple, needed for part 2
    lcm = math.lcm(*[monkey['test'] for monkey in monkeys])

    for _ in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            op = monkeys[i]['operation'][0]
            for item in monkey['items']:
                var = item if monkey['operation'][1] == 'old' else int(monkey['operation'][1])
                if op == '+':
                    new_item = (item + var)%lcm//(3 if divide else 1)
                else:
                    new_item = (item * var)%lcm//(3 if divide else 1)
                monkeys[monkey['if_true' if new_item % monkey['test'] == 0 else 'if_false']]['items'].append(new_item)
            monkey['count'] += len(monkey['items'])
            monkey['items'] = []
    return monkeys

# part 1
monkeys = parse_input()
monkeys = monkey_in_the_middle(monkeys, 20, True)
a, b = sorted([monkey['count'] for monkey in monkeys])[-2:]
print(f'Part 1: {a*b}')

# part 2
monkeys = parse_input()
monkeys = monkey_in_the_middle(monkeys, 10000, False)
a, b = sorted([monkey['count'] for monkey in monkeys])[-2:]
print(f'Part 2: {a*b}')
