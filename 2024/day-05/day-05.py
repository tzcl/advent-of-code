from collections import defaultdict
from functools import cmp_to_key
import itertools as it

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

separator = lines.index("")
rules, updates = lines[:separator], lines[separator + 1 :]

deps = defaultdict(set)
for line in rules:
    if line == "":
        break
    a, b = map(int, line.split("|"))
    deps[a].add(b)

def is_ordered(nums):
    return all(compare(a, b) == -1 for a, b in it.pairwise(nums))

def compare(a, b):
    if b in deps[a]:
        return -1
    elif a in deps[b]:
        return 1
    else:
        return 0

p1 = 0
p2 = 0
for line in updates:
    nums = [int(n) for n in line.split(",")]
    if is_ordered(nums):
        p1 += nums[len(nums) // 2]  # Always odd
        continue

    nums = sorted(nums, key=cmp_to_key(compare))
    p2 += nums[len(nums) // 2]

print(p1)
print(p2)