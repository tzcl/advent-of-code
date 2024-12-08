import sys

sys.setrecursionlimit(10**6)
lines = [line.strip() for line in sys.stdin]

grid = [[c for c in line] for line in lines]
R = len(lines)
assert R > 0
C = len(lines[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
p1 = 0
p2 = 0


sr, sc = 0, 0
for r in range(R):
    for c in range(C):
        if lines[r][c] == "^":
            sr, sc = r, c

visited = set()
seen = set()
r, c, d = sr, sc, 0
while True:
    if (r, c, d) in visited:
        break

    visited.add((r, c, d))
    seen.add((r, c))
    grid[r][c] = "X"

    dr, dc = dirs[d]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < R and 0 <= nc < C):
        p1 = len(seen)
        break
    if grid[nr][nc] == "#":
        d = (d + 1) % 4
    else:
        r, c = nr, nc

print(p1)
for row in grid:
    print("".join(row))
