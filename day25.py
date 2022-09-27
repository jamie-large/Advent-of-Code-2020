def solution_part1():
    with open("inputs/day25.txt", "r") as f:
        card_public_key = int(f.readline())
        door_public_key = int(f.readline())

        card_loop_size = calculate_loop_size(card_public_key)
        door_loop_size = calculate_loop_size(door_public_key)

        print(f"{card_loop_size}, {door_loop_size}")
        print(f"{transform(door_public_key, card_loop_size - 1)}, {transform(card_public_key, door_loop_size - 1)}")


def calculate_loop_size(public_key):
    i = 1
    subject_number = 7
    value = subject_number
    while value != public_key:
        value = (value * subject_number) % 20201227
        i += 1
    return i

def transform(subject_number, loop_size):
    value = subject_number
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value

solution_part1()
