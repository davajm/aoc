tot = 0
cards = {}
with open("inputs/04") as f:
    card = 1
    for line in f.readlines():
        line = line.rstrip("\n")
        winning, have = line.split(" | ")
        winning = set(winning.split(": ")[1].split())
        have = have.split()
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
        match = sum([1 for n in winning if n in have])
        if match:
            tot += 2 ** (match - 1)
            for i in range(1, match + 1):
                if card + i in cards:
                    cards[card + i] += cards[card]
                else:
                    cards[card + i] = cards[card]
        card += 1

print(f"Part 1: {tot}")
print(f"Part 2: {sum(cards.values())}")
