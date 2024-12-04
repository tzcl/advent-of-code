with open("input") as f:
    lines = f.read().splitlines()

dirs = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if not (dr == 0 and dc == 0)]


def part1(lines: list[str]) -> int:
    ans = 0

    m = len(lines)
    n = len(lines[0])

    def valid(row: int, col: int) -> bool:
        return row >= 0 and col >= 0 and row < m and col < n

    def explore(row: int, col: int, dir: tuple[int, int]) -> bool:
        dr, dc = dir
        step = 0

        while valid(row, col) and lines[row][col] == "XMAS"[step]:
            row += dr
            col += dc
            step += 1

            if step == 4:
                return True

        return False

    for row in range(m):
        for col in range(n):
            if lines[row][col] == "X":
                for dir in dirs:
                    if explore(row, col, dir):
                        ans += 1

    return ans


def part2(lines: list[str]) -> int:
    ans = 0

    m = len(lines)
    n = len(lines[0])

    def valid(row: int, col: int) -> bool:
        return row >= 0 and col >= 0 and row < m and col < n

    def explore(row: int, col: int, dir: tuple[int, int], s: str) -> bool:
        dr, dc = dir
        step = 0

        while valid(row, col) and lines[row][col] == s[step]:
            row += dr
            col += dc
            step += 1

            if step == len(s):
                return True

        return False

    for row in range(m - 2):
        for col in range(n - 2):
            if lines[row][col] == "M":
                if explore(row, col, (1, 1), "MAS") and (
                    explore(row, col + 2, (1, -1), "MAS")
                    or explore(row, col + 2, (1, -1), "SAM")
                ):
                    ans += 1
            elif lines[row][col] == "S":
                if explore(row, col, (1, 1), "SAM") and (
                    explore(row, col + 2, (1, -1), "MAS")
                    or explore(row, col + 2, (1, -1), "SAM")
                ):
                    ans += 1

    return ans


print(part1(lines))
print(part2(lines))
