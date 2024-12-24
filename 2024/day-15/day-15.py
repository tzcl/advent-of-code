lines = [line.strip() for line in open("input").readlines()]

grid, moves = [
    lines[: lines.index("")],
    [ch for line in lines[lines.index("") + 1 :] for ch in line],
]

M = len(grid)
N = len(grid[0])

grid = {complex(r, c): ch for r, row in enumerate(grid) for c, ch in enumerate(row)}

scaled = {}
for z in grid:
    r, c = z.real, z.imag
    if grid[z] == "#":
        scaled[complex(r, 2 * c)] = "#"
        scaled[complex(r, 2 * c + 1)] = "#"
    elif grid[z] == "O":
        scaled[complex(r, 2 * c)] = "["
        scaled[complex(r, 2 * c + 1)] = "]"
    elif grid[z] == "@":
        scaled[complex(r, 2 * c)] = "@"
        scaled[complex(r, 2 * c + 1)] = "."
    else:
        scaled[complex(r, 2 * c)] = "."
        scaled[complex(r, 2 * c + 1)] = "."


def print_grid(grid, M, N):
    for r in range(M):
        for c in range(N):
            print(grid[complex(r, c)], end="")
        print()
    print()


print_grid(grid, M, N)
print_grid(scaled, M, 2 * N)


def gps(grid):
    score = 0
    for z in grid:
        if grid[z] in "O[":
            score += z.imag + z.real * 100

    return score


dir = {"^": -1, ">": 1j, "v": 1, "<": -1j}


def run(grid):
    start = next(z for z, ch in grid.items() if ch == "@")
    print("start", start)

    pos = start
    for m in moves:
        d = dir[m]
        np = pos + d
        if grid[np] == "#":
            continue

        stack = []
        box = np
        while grid[box] == "O":
            stack.append(box)
            box += d
        if grid[box] == "#":
            continue

        while stack:
            p = stack.pop()
            grid[box] = "O"
            grid[p] = "."
            box = p

        grid[pos] = "."
        grid[np] = "@"
        pos = np
        print("move", m)
        print_grid(grid, M, N)


def objects(grid, pos, d):
    ahead = pos + d
    result = {pos}
    if grid[ahead] in "[]":
        result |= objects(grid, ahead, d)
    if d.imag == 0:
        if grid[ahead] == "[":
            result |= objects(grid, ahead + 1j, d)
        if grid[ahead] == "]":
            result |= objects(grid, ahead - 1j, d)

    return result


def move_objects(grid, objects, d):
    if any(grid[o + d] == "#" for o in objects):
        return False

    updates = {o + d: grid[o] for o in objects}
    grid.update({o: "." for o in objects})
    grid.update(updates)

    return True


def run_scaled(grid):
    start = next(z for z, ch in grid.items() if ch == "@")
    print("start", start)

    pos = start
    for m in moves:
        d = dir[m]
        np = pos + d
        if grid[np] == "#":
            continue

        o = objects(grid, pos, d)
        if move_objects(grid, o, d):
            pos = np

        print("move", m)
        print_grid(grid, M, 2 * N)


run_scaled(scaled)
print(int(gps(scaled)))
