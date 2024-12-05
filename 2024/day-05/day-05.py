from collections import defaultdict
from functools import cmp_to_key

with open("sample") as f:
    lines = [line.strip() for line in f.readlines()]

separator = lines.index("")
rules, updates = lines[:separator], lines[separator + 1 :]

deps = defaultdict(set)
for line in rules:
    if line == "":
        break
    a, b = map(int, line.split("|"))
    deps[b].add(a)


def valid_deps(n, seen):
    # Given n, check that everything seen so far validates deps
    for s in seen:
        if n in deps[s]:
            return False

    return True


def valid_update(nums):
    seen = []
    for n in nums:
        if not valid_deps(n, seen):
            return False
        else:
            print(n, "valid deps")
        seen.append(n)

    return True


def swap_deps(n, seen):
    # Given n, check that everything seen so far validates deps
    for s in seen:
        if n in deps[s]:
            return seen[s]

    return -1


def fix_update(nums):
    seen = {}
    i = 0
    while i < len(nums):
        j = swap_deps(nums[i], seen)
        seen[nums[i]] = i
        if j >= 0:
            nums[i], nums[j] = nums[j], nums[i]
            seen[nums[i]] = i
            seen[nums[j]] = j
            i = min(i, j)
        else:
            i += 1
            

    return nums

def compare(a, b):
    if a in deps[b]:
        return -1
    elif b in deps[a]:
        return 1
    else:
        return 0

p1 = 0
p2 = 0
for line in updates:
    nums = [int(n) for n in line.split(",")]
    print(nums)
    if valid_update(nums):
        p1 += nums[len(nums) // 2]  # Always odd
        continue

    # Fix the ordering
    # nums = fix_update(nums)
    nums = sorted(nums, key=cmp_to_key(compare))
    p2 += nums[len(nums) // 2]

print(p1)
print(p2)