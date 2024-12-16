import copy
import sys

sys.setrecursionlimit(2147483647)

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

m = len(lines)
n = len(lines[0])

grid = {r * 1j + c: ch for r, line in enumerate(lines) for c, ch in enumerate(line)}


def print_grid(grid):
    for r in range(m):
        for c in range(n):
            print(grid[r * 1j + c], end="")
        print()
    print()


# Max recursion depth reached
def score(grid, pos, dir, acc):
    if grid[pos] == "E":
        # print_grid(grid)
        return acc

    curr = grid[pos]
    grid[pos] = {1: ">", -1j: "^", 1j: "v", -1: "<"}[dir]

    # print_grid(grid)

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


p1 = 0
for r in range(m):
    for c in range(n):
        if grid[r * 1j + c] == "S":
            g = copy.deepcopy(grid)
            p1 = score(g, r * 1j + c, 1, 0)

print(p1)
