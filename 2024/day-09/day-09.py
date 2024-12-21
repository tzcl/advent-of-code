from dataclasses import dataclass


@dataclass(frozen=True)
class Block:
    pos: int
    size: int
    id: int

    def checksum(self) -> int:
        # Returns id * ((pos + 1) + ... + (pos + size))
        return self.id * (2 * self.pos + self.size - 1) * self.size // 2


input = open("input").read().strip()


def parse(input, p1=True):
    files, gaps, p = [], [], 0
    for i, n in enumerate(map(int, input)):
        if p1 and i % 2 == 0:
            files.extend([Block(p + x, 1, i // 2) for x in range(n)])
        else:
            (files, gaps)[i % 2].append(Block(p, n, i // 2))
        p += n

    return files, gaps


def renumerate(sequence):
    """Enumerate a sequence in reverse."""
    return zip(range(len(sequence) - 1, -1, -1), reversed(sequence))


def defrag(files, gaps):
    for i, fb in renumerate(files):
        for j, gb in enumerate(gaps):
            if gb.pos >= fb.pos:
                break
            if gb.size >= fb.size:
                files[i] = Block(gb.pos, fb.size, fb.id)
                gaps[j] = Block(gb.pos + fb.size, gb.size - fb.size, gb.id)
                break


def checksum(files):
    return sum(f.checksum() for f in files)


if __name__ == "__main__":
    fs, gs = parse(input)
    defrag(fs, gs)
    print(checksum(fs))

    fs, gs = parse(input, p1=False)
    defrag(fs, gs)
    print(checksum(fs))
