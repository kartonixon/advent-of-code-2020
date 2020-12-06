answers_by_group = []


def read_input():
    answers = ""
    with open("input.txt") as file:
        n = 0
        for line in file:
            if line.rstrip("\n"):
                answers += line.rstrip("\n")
                n += 1
            else:
                answers_by_group.append({"answers": answers, "people": n})
                answers = ""
                n = 0
        answers_by_group.append({"answers": answers, "people": n})


def part1():
    total = 0
    for group in answers_by_group:
        s = set(group["answers"])
        total += len(s)
    return total


def part2():
    total = 0
    for group in answers_by_group:
        unique = set()
        for letter in group["answers"]:
            if group["answers"].count(letter) == group["people"]:
                unique.add(letter)
        total += len(unique)
    return total


if __name__ == '__main__':
    read_input()
    print(part1(), part2())

