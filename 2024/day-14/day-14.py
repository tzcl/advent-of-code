import re
import math
import collections

lines = [line.strip() for line in open("input").readlines()]

W = 101
H = 103
# W = 11
# H = 7
R = len(lines)

P = []
V = []

for line in lines:
    p, v = [(int(x), int(y)) for x, y in re.findall(r"(-?\d+),(-?\d+)", line)]
    P.append(p)
    V.append(v)


def simulate(P, V, step):
    for i in range(R):
        x, y = P[i]
        dx, dy = V[i]

        x = (x + step * dx) % W
        y = (y + step * dy) % H

        P[i] = x, y


def tree(P, V):
    step = 1
    m = 0
    while step <= 10403:
        simulate(P, V, 1)

        ys = collections.Counter([y for _, y in P])
        m = max(m, max(ys.values()))
        if any(y >= 30 for y in ys.values()):
            print(step)
            visualise(P)
            # return step

        step += 1


def visualise(P):
    s = set(P)
    for y in range(H):
        for x in range(W):
            if (x, y) in s:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def quadrants(P):
    mx, my = W // 2, H // 2
    counts = collections.defaultdict(int)

    for x, y in P:
        if x == mx or y == my:
            continue
        counts[(x < mx, y < my)] += 1

    print(counts)
    return counts


# [print(p) for p in P]
# print()

# visualise(P)

# simulate(P, V, 100)

# [print(p) for p in P]
# print()

# visualise(P)

# print(math.prod(quadrants(P).values()))

steps = tree(P, V)

# simulate(P, V, 10403)

# visualise(P)

print(steps)
