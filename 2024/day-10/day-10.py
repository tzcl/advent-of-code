import copy
import sys
import itertools

# lines = [line.strip() for line in sys.stdin]
with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

m = len(lines)
n = len(lines[0])
grid = {(r, c): ch for r, line in enumerate(lines) for c, ch in enumerate(line)}


def print_grid(grid):
    for r in range(m):
        for c in range(n):
            print(grid[r, c], end="")
        print()
    print()


p1 = 0

dirs = ((1, 0), (-1, 0), (0, -1), (0, 1))


def dfs(grid, r, c, acc):
    if grid[r, c] == "9":
        grid[r, c] = "o"
        print_grid(grid)
        return acc + 1

    curr = int(grid[r, c])
    grid[r, c] = "x"

    print_grid(grid)

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if (nr, nc) not in grid or grid[nr, nc] in (".", "x", "o"):
            continue
        if int(grid[nr, nc]) - curr == 1:
            acc = dfs(grid, nr, nc, acc)

    return acc


for r, c in grid.keys():
    if grid[r, c] == "0":
        g = copy.deepcopy(grid)
        p1 += dfs(g, r, c, 0)

print(p1)


def dfs2(grid, r, c, acc):
    if grid[r, c] == "9":
        print_grid(grid)
        return acc + 1

    curr = int(grid[r, c])
    grid[r, c] = "x"

    print_grid(grid)

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if (nr, nc) not in grid or grid[nr, nc] in (".", "x", "o"):
            continue
        if int(grid[nr, nc]) - curr == 1:
            acc = dfs2(grid, nr, nc, acc)

    grid[r, c] = curr

    return acc


p2 = 0

for r, c in grid.keys():
    if grid[r, c] == "0":
        g = copy.deepcopy(grid)
        p2 += dfs2(g, r, c, 0)

print(p2)
