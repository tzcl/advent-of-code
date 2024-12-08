import sys

sys.setrecursionlimit(10**6)
lines = [line.strip() for line in sys.stdin]

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

for tr in range(R):
    for tc in range(C):
        visited = set()
        seen = set()
        r, c, d = sr, sc, 0
        while True:
            if (r, c, d) in visited:
                p2 += 1
                break

            visited.add((r, c, d))
            seen.add((r, c))

            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                p1 = len(seen)
                break
            if lines[nr][nc] == "#" or (nr, nc) == (tr, tc):
                d = (d + 1) % 4
            else:
                r, c = nr, nc

print(p1)
print(p2)
