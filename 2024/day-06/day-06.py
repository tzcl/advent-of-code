import sys

lines = [line.strip() for line in sys.stdin]

grid = [[c for c in line] for line in lines]
R = len(grid)
assert R > 0
C = len(grid[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def walk(grid):
    r, c, d = sr, sc, 0
    visited = set()
    seen = set()
    while True:
        if (r, c, d) in visited:
            return seen, True

        visited.add((r, c, d))
        seen.add((r, c))

        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            return seen, False
        if grid[nr][nc] == "#":
            d = (d + 1) % 4
        else:
            r, c = nr, nc


sr, sc = 0, 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "^":
            sr, sc = r, c

path = walk(grid)[0]
p1 = len(path)
print(p1)

p2 = 0
for r, c in path:
    ch = grid[r][c]
    grid[r][c] = "#"
    p2 += walk(grid)[1]
    grid[r][c] = ch

print(p2)
