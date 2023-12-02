import sys

def a(lines):
    total = 0
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


numbers = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
]

def b(lines):
    # How can I check if a string contains a dictionary efficiently?
    # Should be able to only perform one pass through the string, do I need a trie?
    total = 0
    for line in lines:
        digits = get_digits(line)
        total += int(digits[0] + digits[-1])
    return total


# TODO: How to optimise?
def get_digits(line):
    digits = []
    for i in range(len(line)):
        if line[i].isdigit(): 
            digits.append(line[i])
        for j, n in enumerate(numbers):
            if i + 2 < len(line): 
                if n == line[i:i+3]: digits.append(str(j+1))
            if i + 3 < len(line): 
                if n == line[i:i+4]: digits.append(str(j+1))
            if i + 4 < len(line): 
                if n == line[i:i+5]: digits.append(str(j+1))
    print(digits)
    return digits


lines = [line.strip() for line in sys.stdin]
print(lines)

print(b(lines))
