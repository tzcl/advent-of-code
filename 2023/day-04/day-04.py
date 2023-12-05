import sys

lines = sys.stdin.readlines()


def points():
    points = 0
    for line in lines:
        matches = parse_card(line) - 1
        if matches >= 0:
            points += 1 << matches
    return points


def scorecards():
    copies = [1 for _ in lines]
    for i, line in enumerate(lines):
        matches = parse_card(line)
        for j in range(matches):
            copies[i + j + 1] += copies[i]

    return sum(copies)


def parse_card(line):
    line = line.split(":")[1]
    winners, numbers = line.split("|")
    winners, numbers = winners.split(), numbers.split()
    return len(set(winners) & set(numbers))


print(points(), scorecards())
