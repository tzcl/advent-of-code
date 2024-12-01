import sys

lines = [line.strip() for line in sys.stdin]
print(lines)

left = []
right = []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

print(left, right)

left.sort()
right.sort()

sum = 0
for l, r in zip(left, right):
    sum += abs(l - r)

print(sum)

from collections import Counter

c = Counter(right)

score = 0
for l in left:
    if l in c:
        score += l * c[l]

print(score)
