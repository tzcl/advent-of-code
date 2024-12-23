import numpy as np
import re

lines = [line.strip() for line in open("input").readlines()]
list(map(print, lines))
print()

A = []
B = []
PRIZE = []
N = 1

for line in lines:
    if line == "":
        N += 1
        continue

    nums = list(map(int, re.findall(r"(\d+)", line)))
    if line.startswith("Button A"):
        A.append(nums)
    elif line.startswith("Button B"):
        B.append(nums)
    else:
        nums = list(n + 10000000000000 for n in nums)
        PRIZE.append(nums)

print(A)
print(B)
print(PRIZE)
print()

p1 = 0

for i in range(N):
    buttons = np.array([A[i], B[i]]).T
    det = int(round(np.linalg.det(buttons)))
    raw = np.array([[B[i][1], -B[i][0]], [-A[i][1], A[i][0]]])
    prize = np.array(PRIZE[i])

    soln = raw @ prize
    if np.all(soln % det == 0):
        s = soln / det
        print("solution for", i, s)
        cost = np.dot([3, 1], s)
        p1 += int(np.round(cost))
    else:
        print("no solution for", i)

print(p1)
