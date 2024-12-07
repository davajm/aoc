from itertools import product

eqs = []
with open("inputs/07") as f:
    for line in f.readlines():
        a, b = line.rstrip().split(": ")
        b = [int(x) for x in b.split(" ")]
        eqs.append((int(a), b))


def solve(ops):
    tot = 0
    for n, nums in eqs:
        for prod in list(product(ops, repeat=len(nums) - 1)):
            x = nums[0]
            for i in range(1, len(nums)):
                if prod[i - 1] == "+":
                    x += nums[i]
                elif prod[i - 1] == "*":
                    x *= nums[i]
                elif prod[i - 1] == "||":
                    x = int(str(x) + str(nums[i]))
            if x == n:
                tot += x
                break
    return tot


print(f"Part 1: {solve(['+', '*'])}")
print(f"Part 2: {solve(['+', '*', '||'])}")
