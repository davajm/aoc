totals = []
current = 0

with open('inputs/01') as f:
    for line in f.readlines():
        if line == '\n':
            totals.append(current)
            current = 0
        else:
            current += int(line.strip())

print(f"Max: {max(totals)}")
print(f"Sum top 3: {sum(sorted(totals)[-3:])}")
