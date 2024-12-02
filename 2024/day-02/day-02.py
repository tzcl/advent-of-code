import sys

lines = [line.strip() for line in sys.stdin]


def safe(line):
    report = [int(n) for n in line.split()]
    diff = [report[i] - report[i - 1] for i in range(1, len(report))]
    return all(0 < d <= 3 for d in diff) or all(-3 <= d < 0 for d in diff)


print(sum([safe(line) for line in lines]))


def check_report(report):
    diff = [report[i] - report[i - 1] for i in range(1, len(report))]
    return all(0 < d <= 3 for d in diff) or all(-3 <= d < 0 for d in diff)


def safe2(line):
    report = [int(n) for n in line.split()]
    for i in range(len(report)):
        if check_report(report[:i] + report[i + 1 :]):
            return True

    return False


print(sum(safe2(line) for line in lines))
