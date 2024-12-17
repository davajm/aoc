with open("inputs/16") as f:
    grid = [[x for x in line.rstrip("\n")] for line in f.readlines()]

graph = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != "#":

            # Build graph..
            graph[(i, j, 0)] = [] # up
            graph[(i, j, 1)] = [] # right
            graph[(i, j, 2)] = [] # down
            graph[(i, j, 3)] = [] # left

            if i - 1 >= 0 and grid[i - 1][j] != "#":
                graph[(i, j, 0)].append((1, (i - 1, j, 0)))
                graph[(i, j, 1)].append((1001, (i - 1, j, 0)))
                graph[(i, j, 2)].append((2001, (i - 1, j, 0)))
                graph[(i, j, 3)].append((1001, (i - 1, j, 0)))
            if j + 1 < len(grid[0]) and grid[i][j + 1] != "#":
                graph[(i, j, 0)].append((1001, (i, j + 1, 1)))
                graph[(i, j, 1)].append((1, (i, j + 1, 1)))
                graph[(i, j, 2)].append((1001, (i, j + 1, 1)))
                graph[(i, j, 3)].append((2001, (i, j + 1, 1)))
            if i + 1 < len(grid) and grid[i + 1][j] != "#":
                graph[(i, j, 0)].append((2001, (i + 1, j, 2)))
                graph[(i, j, 1)].append((1001, (i + 1, j, 2)))
                graph[(i, j, 2)].append((1, (i + 1, j, 2)))
                graph[(i, j, 3)].append((1001, (i + 1, j, 2)))
            if j - 1 >= 0 and grid[i][j - 1] != "#":
                graph[(i, j, 0)].append((1001, (i, j - 1, 3)))
                graph[(i, j, 1)].append((2001, (i, j - 1, 3)))
                graph[(i, j, 2)].append((1001, (i, j - 1, 3)))
                graph[(i, j, 3)].append((1, (i, j - 1, 3)))

        if grid[i][j] == "S":
            start = (i, j, 1)
        if grid[i][j] == "E":
            ends = [(i, j, 0), (i, j, 1), (i, j, 2), (i, j, 3)]


# Dijsktra, we meet again.. Ty copilot for the code!
# Note: Modified to also return all paths with the minimum distance
# Note: Not optimized...
def dijkstra(graph, start, ends):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [[start]]

    unvisited = {node for node in graph}

    while unvisited:
        current_node = min(unvisited, key=lambda x: distances[x])
        current_distance = distances[current_node]

        if current_distance == float("inf"):
            break

        for weight, neighbor in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = [path + [neighbor] for path in paths[current_node]]
            elif distance == distances[neighbor]:
                paths[neighbor].extend([path + [neighbor] for path in paths[current_node]])

        unvisited.remove(current_node)

    min_distance = min(distances[end] for end in ends if distances[end] != float("inf"))
    all_paths = []
    for end in ends:
        if distances[end] == min_distance:
            all_paths.extend(paths[end])

    return min_distance, all_paths

tot, paths = dijkstra(graph, start, ends)
print(f"Part 1: {tot}")

tiles = set()
for path in paths:
    for x, y, d in path:
        tiles.add((x, y))

print(f"Part 2: {len(tiles)}")
