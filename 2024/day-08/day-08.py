import itertools

lines = [line.strip() for line in open("input").readlines()]

m = len(lines)
n = len(lines[0])

grid = {complex(r, c): ch for r, row in enumerate(lines) for c, ch in enumerate(row)}


def print_grid():
    for r in range(m):
        for c in range(n):
            print(grid[complex(r, c)], end="")
        print()
    print()


print_grid()

freqs = [[] for _ in range(256)]  # There as 256 ASCII characters

for z in [complex(r, c) for r in range(m) for c in range(n)]:
    if grid[z] == ".":
        continue
    freqs[ord(grid[z])].append(z)

p1 = set()
p2 = set()

for freq in freqs:
    for a, b in itertools.permutations(freq, 2):
        v = b - a
        curr = a + 2 * v
        if curr in grid:
            grid[curr] = "#"
            p1.add(curr)
        curr = a + v
        while curr in grid:
            grid[curr] = "#"
            p2.add(curr)
            curr += v


print_grid()
print(len(p1))
print(len(p2))
