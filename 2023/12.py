records = []
with open("inputs/12") as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        a, b = line.split(' ')
        records.append((a, list(map(int, b.split(',')))))

x = set()
for i in records:
    x.add(''.join([str(c) for c in i[1]]))
print(len(x))
print(len(records))

