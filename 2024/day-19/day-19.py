# NOTE: Need re2 to avoid exponential backtracking
import re2
import functools

patterns, designs = [section for section in open("input").read().split("\n\n")]

patterns = set(patterns.split(", "))
designs = designs.splitlines()


# First approach using regular expressions
# towels = re2.compile(f"({"|".join(patterns)})*")
# print(sum(towels.fullmatch(d) is not None for d in designs))


# Second approach using top-down dp
@functools.cache
def count(d):
    if d == "":
        return 1

    c = 0
    for p in patterns:
        if d.startswith(p):
            c += count(d.removeprefix(p))

    return c


# Third approach using bottom-up dp
def count2(d):
    n = len(d) + 1
    dp = [0] * n
    dp[0] = 1

    for i in range(n):
        for p in patterns:
            l = len(p)
            if i + l <= len(d) and d[i : i + l] == p:
                dp[i + l] += dp[i]

    return dp[len(d)]


print(sum(count(d) for d in designs))
print(sum(count2(d) for d in designs))

# TODO: Use a trie
