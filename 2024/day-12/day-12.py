lines = [line.strip() for line in open("sample3").readlines()]

M = len(lines)
N = len(lines[0])

grid = {complex(r, c): ch for r, row in enumerate(lines) for c, ch in enumerate(row)}


def print_grid(grid):
    for r in range(M):
        for c in range(N):
            print(grid[complex(r, c)], end="")
        print()
    print()


print_grid(grid)


def region(z, seen, r):
    if z not in seen:
        seen.add(z)
        r.add(z)
        for w in (z + 1, z + 1j, z - 1, z - 1j):
            if w not in seen and w in grid and grid[w] == grid[z]:
                region(w, seen, r)

    return r


def perimeter(region):
    p = 0
    for z in region:
        neighbours = 4
        for w in (z + 1, z + 1j, z - 1, z - 1j):
            if w in region:
                neighbours -= 1
        p += neighbours

    return p


def corners(region):
    c = 0
    for z in region:
        for d in (1, 1j, -1, -1j):
            u = z + d
            v = z + d * 1j
            w = z + d + d * 1j
            if (u not in region and v not in region) or (
                u in region and v in region and w not in region
            ):
                c += 1

    return c


seen = set()
p1, p2 = 0, 0

for z in grid.keys():
    if z not in seen:
        r = region(z, seen, set())

        p = perimeter(r)
        c = corners(r)
        p1 += len(r) * p
        p2 += len(r) * c

print(p1)
print(p2)
