with open("input") as f:
    lines = f.read().splitlines()

dial = 50
p1 = p2 = 0


for line in lines:
    dir, dist = line[0], int(line[1:])

    print(dial)
    if dir == "R":
        p2 += ((100 + dial) % 100 + dist) // 100
        dial = (dial + dist) % 100

    elif dir == "L":
        p2 += ((100 - dial) % 100 + dist) // 100
        dial = (dial - dist) % 100

    p1 += dial == 0

print(p1)
print(p2)
