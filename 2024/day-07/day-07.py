import sys
import re
from collections import deque

# lines = [line.strip() for line in sys.stdin]
with open("sample") as f:
    lines = [line.strip() for line in f.readlines()]


def process(line):
    nums = re.findall(r"\d+", line)
    ans, terms = int(nums[0]), [int(n) for n in nums[1:]]

    n = len(terms)

    queue = deque([(terms[0], 1)])

    while queue:
        value, depth = queue.popleft()

        if depth == n:
            if value == ans:
                return ans
        elif depth < n:
            next = terms[depth]
            queue.append((value + next, depth + 1))
            queue.append((value * next, depth + 1))
            # p2
            queue.append((int(str(value) + str(next)), depth + 1))

    return 0


print(sum([process(line) for line in lines]))
