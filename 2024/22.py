with open("inputs/22") as f:
    secrets = [int(line.strip()) for line in f.readlines()]

prices = [[int(str(secret)[-1]) for secret in secrets]]
n = 2000

for j in range(n):
    price_row = []
    for i in range(len(secrets)):
        secret = secrets[i]

        secret ^= secret * 64
        secret %= 16777216

        secret ^= int(secret / 32)
        secret %= 16777216

        secret ^= secret * 2048
        secret %= 16777216

        secrets[i] = secret

        # Store price for part 2
        price_row.append(int(str(secret)[-1]))
    prices.append(price_row)

print(f"Part 1: {sum(secrets)}")

# Part 2
price_mapper, visited = {}, set()

for i in range(4, len(prices)):
    for j in range(len(prices[i])):
        last_5 = tuple(prices[i + k][j] for k in range(-4, 1))
        changes = tuple(last_5[k] - last_5[k - 1] for k in range(1, 5))
        if (changes, j) not in visited:
            visited.add((changes, j))
            if changes in price_mapper:
                price_mapper[changes] += last_5[4]
            else:
                price_mapper[changes] = last_5[4]

print(f"Part 2: {max(price_mapper.values())}")
