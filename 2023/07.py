hands = {}

with open("inputs/07") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        hand, bid = line.split()
        if hand in hands:
            print("lol")
        hands[hand] = int(bid)

card_rank = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5}
rank = 6
for i in range(9, 1, -1):
    card_rank[str(i)] = rank
    rank += 1


def get_hand_type(hand):
    counter = {}
    for card in hand:
        if card not in counter:
            counter[card] = 1
        else:
            counter[card] += 1

    if len(counter) == 1:
        hand_type = 1
    elif 4 in counter.values():
        hand_type = 2
    elif 3 in counter.values() and 2 in counter.values():
        hand_type = 3
    elif 3 in counter.values():
        hand_type = 4
    elif len([x for x in counter.values() if x == 2]) == 2:
        hand_type = 5
    elif 2 in counter.values():
        hand_type = 6
    else:
        hand_type = 7

    return (hand_type,) + tuple(card_rank[card] for card in hand)


rank = 1
tot = 0
for hand in sorted(hands.keys(), key=lambda x: get_hand_type(x))[::-1]:
    tot += hands[hand] * rank
    rank += 1
print(f"Part 1: {tot}")


# Part 2
card_rank = {"A": 1, "K": 2, "Q": 3, "T": 4}
rank = 5
for i in range(9, 1, -1):
    card_rank[str(i)] = rank
    rank += 1
card_rank["J"] = rank


def get_hand_type(hand):
    counter = {}
    jokers = 0
    for card in hand:
        if card == "J":
            jokers += 1
        elif card not in counter:
            counter[card] = 1
        else:
            counter[card] += 1

    max_cards = max(counter.values()) if counter.values() else 0

    if len(counter) == 1 or (jokers + max_cards == 5):
        hand_type = 1
    elif 4 in counter.values() or (jokers + max_cards) == 4:
        hand_type = 2
    elif (
        3 in counter.values()
        and 2 in counter.values()
        or (len([x for x in counter.values() if x == 2]) == 2 and jokers == 1)
    ):
        hand_type = 3
    elif (
        3 in counter.values()
        or (2 in counter.values() and jokers == 1)
        or (1 in counter.values() and jokers == 2)
    ):
        hand_type = 4
    elif len([x for x in counter.values() if x == 2]) == 2:
        hand_type = 5
    elif 2 in counter.values() or jokers > 0:
        hand_type = 6
    else:
        hand_type = 7

    return (hand_type,) + tuple(card_rank[card] for card in hand)


rank = 1
tot = 0
for hand in sorted(hands.keys(), key=lambda x: get_hand_type(x))[::-1]:
    tot += hands[hand] * rank
    rank += 1
print(f"Part 2: {tot}")
