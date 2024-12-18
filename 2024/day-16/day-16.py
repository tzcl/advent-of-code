import copy
import heapq
import itertools

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

m = len(lines)
n = len(lines[0])

grid = {complex(c, r): ch for r, line in enumerate(lines) for c, ch in enumerate(line)}


def print_grid(grid):
    for r in range(m):
        for c in range(n):
            print(grid[r * 1j + c], end="")
        print()
    print()


# Max recursion depth reached
def score(grid, pos, dir, acc):
    if grid[pos] == "E":
        print_grid(grid)
        return acc

    curr = grid[pos]
    grid[pos] = {1: ">", -1j: "^", 1j: "v", -1: "<"}[dir]

    print_grid(grid)

    scores = []

    next = pos + dir
    if next in grid and grid[next] in (".", "E"):
        scores.append(score(grid, next, dir, acc + 1))

    dir *= -1j
    next = pos + dir
    if next in grid and grid[next] in (".", "E"):
        scores.append(score(grid, next, dir, acc + 1001))

    dir *= -1
    next = pos + dir
    if next in grid and grid[next] in (".", "E"):
        scores.append(score(grid, next, dir, acc + 1001))

    grid[pos] = curr

    return min(scores) if scores else 2**1000


def dijkstra(grid, start):
    queue = []
    counter = itertools.count()

    # Complex numbers aren't comparable using <
    # Therefore, we sort based on score and used insertion order to break ties
    heapq.heappush(queue, (0, next(counter), start, 1))

    while queue:
        score, _, pos, dir = heapq.heappop(queue)

        if grid[pos] == "E":
            return score

        grid[pos] = "#"

        for d in (1, -1j, 1j):
            s = 1
            if d.imag != 0:
                s += 1000
            nd = dir * d
            np = pos + nd
            if np in grid and grid[np] != "#":
                heapq.heappush(queue, (score + s, next(counter), np, nd))

    # No path exists
    return -1


p1 = 0
for r in range(m):
    for c in range(n):
        if grid[r * 1j + c] == "S":
            g = copy.deepcopy(grid)
            p1 = dijkstra(g, r * 1j + c)

print(p1)


def paths(grid, start, target):
    queue = []
    counter = itertools.count()

    # Complex numbers aren't comparable using <
    # Therefore, we sort based on score and used insertion order to break ties
    heapq.heappush(queue, (0, next(counter), [start], 1))

    dist = {(start, 1): 0}

    paths = []
    min_score = float("inf")

    while queue:
        score, _, path, dir = heapq.heappop(queue)
        pos = path[-1]

        if grid[pos] == target:
            if score <= min_score:
                min_score = score
                paths.append(path)

        for d, s in (1, 1), (-1j, 1001), (1j, 1001):
            nd = dir * d
            np = pos + nd
            if np in grid and grid[np] != "#":
                if (np, nd) not in dist or score + s <= dist[np, nd]:
                    dist[np, nd] = score + s
                    heapq.heappush(queue, (score + s, next(counter), path + [np], nd))

    return set([pos for path in paths for pos in path])


p2 = 0
for r in range(m):
    for c in range(n):
        if grid[complex(c, r)] == "S":
            g = copy.deepcopy(grid)
            p2 = len(paths(g, complex(c, r), "E"))

print(p2)
