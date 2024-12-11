from functools import lru_cache

with open("inputs/11") as f:
    stones = [int(x) for x in f.readline().split(" ")]


@lru_cache(maxsize=None)
def blink(stone, n):
    if n == 0:
        return 1
    if stone == 0:
        return blink(1, n - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        a, b = stone_str[: len(stone_str) // 2], stone_str[len(stone_str) // 2 :]
        return blink(int(a), n - 1) + blink(int(b), n - 1)
    else:
        return blink(stone * 2024, n - 1)


# Part 1
tot = sum([blink(stone, 25) for stone in stones])
print(f"Part 1: {tot}")

# Part 2
tot = sum([blink(stone, 75) for stone in stones])
print(f"Part 2: {tot}")
