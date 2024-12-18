from collections import deque

bytes = []
with open("inputs/18") as f:
    for line in f.readlines():
        x, y = map(int, line.strip().split(","))
        bytes.append((x, y))


def solve(grid_size, byte_size):
    # Fill grid with bytes
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(0, byte_size):
        x, y = bytes[i]
        grid[y][x] = "#"

    queue = deque([(0, 0, 0)])
    end = (grid_size - 1, grid_size - 1)

    paths = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    visited = set()

    while queue:
        x, y, steps = queue.popleft()
        visited.add((x, y))

        # Traverse neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                nx < 0
                or ny < 0
                or nx >= len(grid)
                or ny >= len(grid[0])
                or (nx, ny) in visited
                or grid[nx][ny] == "#"
            ):
                continue

            if (nx, ny) == end:
                return steps + 1
            visited.add((nx, ny))
            paths[nx][ny] = steps + 1
            queue.append((nx, ny, steps + 1))
    return -1


GRID_SIZE = 71
BYTE_SIZE = 1024

print(f"Part 1: {solve(GRID_SIZE, BYTE_SIZE)}")

for i in range(BYTE_SIZE, len(bytes)):
    if solve(71, i) == -1:
        x, y = bytes[i - 1]
        print(f"Part 2: {x},{y}")
        break
