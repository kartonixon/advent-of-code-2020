m = []


def read_input():
    with open("input.txt") as file:
        for line in file:
            m.append(line.strip("\n"))


def check_slope(h, v):
    trees = x = y = 0
    while y < len(m):
        if m[y][x] == "#":
            trees += 1
        x = (x + h) % len(m[y])
        y += v
    return trees


if __name__ == '__main__':
    read_input()
    print(check_slope(3, 1))
    print(check_slope(1, 1)*check_slope(3, 1)*check_slope(5, 1)*check_slope(7, 1)*check_slope(1, 2))
