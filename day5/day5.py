seat_strings = []
seat_ids = []


def read_input():
    with open("input.txt") as file:
        for line in file:
            seat_strings.append(line.rstrip("\n"))


def highest_seat_id():
    highest = 0
    for boarding_pass in seat_strings:
        row = 0
        base = 64
        for letter in boarding_pass[:7]:
            if letter == "B":
                row += base
            base /= 2
        col = 0
        base = 4
        for letter in boarding_pass[7:]:
            if letter == "R":
                col += base
            base /= 2
        seat_id = int(row * 8 + col)
        seat_ids.append(seat_id)
        if seat_id > highest:
            highest = seat_id
    return highest


def find_seat():
    for i in range(8, 121):
        for j in range(7):
            seat_id = i * 8 + j
            if seat_id not in seat_ids:
                if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
                    return seat_id


if __name__ == '__main__':
    read_input()
    print(highest_seat_id(), find_seat())
