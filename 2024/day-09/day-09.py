import itertools

input = open("sample").read().strip()


def parse(input: str) -> list[str]:
    memory = []
    counter = itertools.count()

    for i, s in enumerate(input):
        n = int(s)
        ch = "."
        if i % 2 == 0:
            ch = str(next(counter))
        memory.extend([ch] * n)

    return memory


def defrag(memory: list[str]) -> list[str]:
    free = memory.index(".")
    i = len(memory) - 1
    while i >= 0 and memory[i] == ".":
        i -= 1

    while free < i:
        memory[i], memory[free] = memory[free], memory[i]
        while free < len(memory) and memory[free] != ".":
            free += 1
        while i >= 0 and memory[i] == ".":
            i -= 1

    return memory


def checksum(memory: list[str]) -> int:
    acc = 0

    for i, s in enumerate(memory):
        if s == ".":
            break
        n = int(s)
        acc += i * n

    return acc


if __name__ == "__main__":
    print(input)

    memory = parse(input)
    print(memory)

    defragged = defrag(memory)
    print(defragged)

    c = checksum(defragged)
    print(c)
