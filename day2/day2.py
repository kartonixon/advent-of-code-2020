part_1 = part_2 = 0

with open("input.txt") as file:
    for line in file:
        a, b, c = line.split();

        # PART 1
        x, y = map(int, a.split("-"))
        if c.count(b[0]) in range(x, y + 1):
            part_1 += 1

        # PART 2
        x, y = map(lambda n: n - 1, map(int, a.split("-")))
        if (c[x] != c[y]) and (c[x] == b[0] or c[y] == b[0]):
            part_2 += 1

print(part_1, part_2)
