def solution_part1():
    with open("inputs/day24.txt", "r") as f:
        flipped_tiles = set()
        for line in f:
            current_tile = [0, 0]
            i = 0
            while i < len(line) - 1:
                if line[i] == "e":
                    current_tile[0] += 2
                    i += 1
                elif line[i:i+2] == "se":
                    current_tile[0] += 1
                    current_tile[1] -= 1
                    i += 2
                elif line[i:i+2] == "sw":
                    current_tile[0] -= 1
                    current_tile[1] -= 1
                    i += 2
                elif line[i] == "w":
                    current_tile[0] -= 2
                    i += 1
                elif line[i:i+2] == "nw":
                    current_tile[0] -= 1
                    current_tile[1] += 1
                    i += 2
                elif line[i:i+2] == "ne":
                    current_tile[0] += 1
                    current_tile[1] += 1
                    i += 2
                else:
                    print("FUCK!!!!")
                    return
            ct = tuple(current_tile)
            if ct in flipped_tiles:
                flipped_tiles.remove(ct)
            else:
                flipped_tiles.add(ct)

        print(len(flipped_tiles))
        return flipped_tiles


def solution_part2():
    with open("inputs/day24.txt", "r") as f:
        flipped_tiles = solution_part1()
        for i in range(100):
            flipped_tiles = get_next_flipped(flipped_tiles)
        print(len(flipped_tiles))

neighbor_offsets = [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]

def get_next_flipped(flipped_tiles):
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    for (x, y) in flipped_tiles:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    black_tiles = set()
    white_tiles = [(x, y) for x in range(min_x - 2, max_x + 3) for y in range(min_y - 1, max_y + 2) if (x, y) not in flipped_tiles]
    for (x, y) in flipped_tiles:
        black_neighbors = [True for (x_offset, y_offset) in neighbor_offsets if (x + x_offset, y + y_offset) in flipped_tiles]
        if len(black_neighbors) in (1, 2):
            black_tiles.add((x, y))
    for (x, y) in white_tiles:
        black_neighbors = [True for (x_offset, y_offset) in neighbor_offsets if (x + x_offset, y + y_offset) in flipped_tiles]
        if len(black_neighbors) == 2:
            black_tiles.add((x, y))

    return black_tiles


solution_part2()
