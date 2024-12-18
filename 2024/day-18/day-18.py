from collections import deque
import itertools

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

N = 71

input = [["." for _ in range(N)] for _ in range(N)]

for line in lines[:1024]:
    x, y = map(int, line.split(","))
    input[y][x] = "#"

for row in input:
    for col in row:
        print(col, end="")
    print()

grid = {
    complex(r, c): ch
    for r, line in enumerate(input)
    for c, ch in enumerate(line)
    if ch != "#"
}


def bfs(grid):
    queue = deque()
    queue.append((0, 0))

    seen = set()
    seen.add(0)

    last = 0

    while queue:
        cur, steps = queue.popleft()
        last = cur

        if cur == complex(N - 1, N - 1):
            return steps, True

        for d in (1, 1j, -1, -1j):
            nxt = cur + d
            if nxt in grid and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, steps + 1))

    return last, False


print("p1", bfs(grid))

print("doing p2")

input2 = [["." for _ in range(N)] for _ in range(N)]
grid2 = {complex(r, c): "." for r in range(N) for c in range(N)}
counter = itertools.count()

for line in lines:
    x, y = map(int, line.split(","))
    input2[y][x] = "#"
    del grid2[complex(x, y)]

    pos, success = bfs(grid2)
    if not success:
        print("p2", line)
        break
else:
    print("all paths succeed??")
