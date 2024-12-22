import collections
import functools

stones = [int(n) for n in open("input").read().split()]
print(stones)


# Actually generate the stones at each step
def generate(stones):
    new = []

    for stone in stones:
        if stone == 0:
            new.append(1)
        elif len(str(stone)) % 2 == 0:
            ss = str(stone)
            m = len(ss) // 2
            left, right = ss[:m], ss[m:]
            new.append(int(left))
            new.append(int(right))
        else:
            new.append(stone * 2024)

    return new


# Based on the observation there aren't that many distinct values a stone can
# take on, we can optimise by operating on all stones of the same value at
# the same time. (This works because order doesn't matter.)
def count(counter):
    c = dict(counter)
    for stone, n in c.items():
        if stone == 0:
            counter[stone] -= n
            counter[1] += n
        elif len(str(stone)) % 2 == 0:
            ss = str(stone)
            m = len(ss) // 2
            left, right = int(ss[:m]), int(ss[m:])
            counter[stone] -= n
            counter[left] += n
            counter[right] += n
        else:
            counter[stone] -= n
            counter[stone * 2024] += n


# Count the number of stones each stone produces after d steps
@functools.cache
def memo(stone, s):
    if s == 0:
        return 1
    if stone == 0:
        return memo(1, s - 1)
    if len(str(stone)) % 2 == 0:
        ss = str(stone)
        m = len(ss) // 2
        left, right = int(ss[:m]), int(ss[m:])
        return memo(left, s - 1) + memo(right, s - 1)

    return memo(stone * 2024, s - 1)


# 1. Generating all values
# for i in range(25):
#     stones = generate(stones)
#     print(i, len(stones))

# print(len(stones))

# 2. Using a counter of all values
# counter = collections.Counter(stones)
# for i in range(75):
#     count(counter)

# print(sum(counter.values()))

# 3. Using memoization
print(sum(map(lambda s: memo(s, 75), stones)))
