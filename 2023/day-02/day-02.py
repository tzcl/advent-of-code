import sys
import re
import collections
import math

lines = []
for line in sys.stdin:
    lines.append(line)


num_red = 12
num_green = 13
num_blue = 14


def a(lines):
    total = 0
    for line in lines:
        total += parse_line(line)
    return total


def b(lines):
    total = 0
    for line in lines:
        total += parse_line2(line)
    return total


def parse_line(line):
    game, revealed = line.split(sep=":")
    id = int(re.match("Game (\d+)", game).group(1))
    bags = collections.defaultdict(int)
    for num, col in re.findall("(\d+) (\w+)", revealed):
        bags[col] = max(bags[col], int(num))
    if bags["red"] <= num_red and bags["green"] <= num_green and bags["blue"] <= num_blue:
        return id
    return 0


def parse_line2(line):
    bags = collections.defaultdict(int)
    for num, col in re.findall("(\d+) (\w+)", line):
        bags[col] = max(bags[col], int(num))
    # if bags["red"] <= num_red and bags["green"] <= num_green and bags["blue"] <= num_blue:
    #     return id
    return math.prod(bags.values())


print(b(lines))
