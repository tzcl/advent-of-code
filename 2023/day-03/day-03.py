import sys
import collections

# How do other people read in input?
# How should I structure my files?
lines = []
for line in sys.stdin:
    lines.append(line)


def sum_parts(lines):
    total = 0
    for row in range(len(lines)):
        line = lines[row]
        state = "special"
        num = 0
        valid = False
        for col in range(len(line)):
            c = line[col]
            match state:
                case "special":
                    if c.isdigit():
                        num = int(c)
                        if not valid:
                            valid = validate(lines, row, col)
                        state = "number"
                case "number":
                    if c.isdigit():
                        num = num * 10 + int(c)
                        if not valid:
                            valid = validate(lines, row, col)
                    else:
                        if valid:
                            total += num
                            valid = False
                        num = 0
                        state = "special"

    return total


dirs = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0]


def is_symbol(char):
    return not char.isdigit() and char not in [".", "\n"]


def validate(lines, row, col, fn=is_symbol):
    for dr, dc in dirs:
        if dr == 0 and dc == 0:
            continue
        nr, nc = row + dr, col + dc
        if nr < 0 or nr >= len(lines) or nc < 0 or nc >= len(lines[nr]):
            continue
        if fn(lines[nr][nc]):
            return (True, (nr, nc))

    return (False, (-1, -1))


def sum_gear_ratios(lines):
    ratios = collections.defaultdict(list)
    for row in range(len(lines)):
        line = lines[row]
        state = "special"
        num = 0
        pos = ()
        valid = False
        for col in range(len(line)):
            c = line[col]
            match state:
                case "special":
                    if c.isdigit():
                        num = int(c)
                        if not valid:
                            valid, pos = validate(lines, row, col, is_gear)
                        state = "number"
                case "number":
                    if c.isdigit():
                        num = num * 10 + int(c)
                        if not valid:
                            valid, pos = validate(lines, row, col, is_gear)
                    else:
                        if valid:
                            ratios[pos].append(num)
                            valid = False
                        num = 0
                        pos = ()
                        state = "special"

    total = 0
    for pos, numbers in ratios.items():
        if len(numbers) == 2:
            print("gear", pos)
            total += numbers[0] * numbers[1]
    return total


def is_gear(char):
    return char == "*"


# print(sum_parts(lines))
print(sum_gear_ratios(lines))
