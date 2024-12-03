import sys
import re

data = sys.stdin.read()

p1 = 0
p2 = 0

matches = re.findall(r"mul\((\d+),(\d+)\)", data)
for a, b in matches:
    p1 += int(a) * int(b)

print(p1)

enabled = True
matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", data)
for m in matches:
    if m.startswith("mul") and enabled:
        a, b = re.findall(r"\d+", m)
        p2 += int(a) * int(b)
    elif m == "don't()":
        enabled = False
    elif m == "do()":
        enabled = True

print(p2)
