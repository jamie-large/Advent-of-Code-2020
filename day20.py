def solution_part1():
    with open('inputs/day20.txt', 'r') as f:
        current_tile = None
        tiles = {}
        for line in f:
            if line[:4] == "Tile":
                current_tile = (int(line.split()[-1][:-1]), [])
            elif len(line) > 1:
                current_tile[1].append(line[:-1])
            else:
                tiles[current_tile[0]] = current_tile[1]
        tiles[current_tile[0]] = current_tile[1]

        tile_edges = {}
        for t in tiles:
            grid = tiles[t]
            edges = [grid[0], "".join([x[-1] for x in grid]), grid[-1], "".join([x[0] for x in grid])]
            edges = edges + [x[::-1] for x in edges]
            tile_edges[t] = edges

        matches = {}
        for t1 in tiles:
            for t2 in tiles:
                if t1 == t2:
                    continue
                t1_edges = tile_edges[t1]
                t2_edges = tile_edges[t2]
                for i in range(len(t1_edges)):
                    edge = t1_edges[i]
                    if edge in t2_edges:
                        if t1 not in matches:
                            matches[t1] = []
                        matches[t1].append((t2, edge, i, t2_edges.index(edge)))

        corner_pieces = []
        edge_pieces = []
        middle_pieces = []
        for t in matches:
            matched_edges = set(x[1] for x in matches[t])
            unmatched_edges = [x for x in tile_edges[t] if x not in matched_edges]
            if len(unmatched_edges) == 4:
                corner_pieces.append(t)
            elif len(unmatched_edges) == 2:
                edge_pieces.append(t)
            else:
                middle_pieces.append(t)

        result = 1
        for i in corner_pieces:
            result *= i
        print(result)

        return tiles, matches, corner_pieces, edge_pieces, middle_pieces




def solution_part2():
    tiles, matches, corner_pieces, edge_pieces, middle_pieces = solution_part1()

    # BEGIN SOLVING THE PUZZLE - put a corner in the top left
    solved_puzzle = [[corner_pieces[0]]]
    corner_pieces.pop(0)

    # Solve the top edge
    current_piece = solved_puzzle[0][0]
    current_matches = matches[current_piece]
    while not any(x[0] in corner_pieces for x in current_matches):
        next_piece = [x[0] for x in current_matches if x[0] in edge_pieces][0]
        solved_puzzle[0].append(next_piece)
        edge_pieces.remove(next_piece)
        current_piece = next_piece
        current_matches = matches[current_piece]
    next_corner = [x[0] for x in current_matches if x[0] in corner_pieces][0]
    solved_puzzle[0].append(next_corner)
    corner_pieces.remove(next_corner)
    current_piece = next_corner
    current_matches = matches[current_piece]

    # Fill out rest of puzzle
    num_remaining_pieces = len(corner_pieces) + len(edge_pieces) + len(middle_pieces)
    for _ in range(int(num_remaining_pieces / len(solved_puzzle[0]))):
        solved_puzzle.append([-1 for _ in range(len(solved_puzzle[0]))])

    current_row = 1
    # Solve the right edge
    while not any(x[0] in corner_pieces for x in current_matches):
        next_piece = [x[0] for x in current_matches if x[0] in edge_pieces][0]
        solved_puzzle[current_row][-1] = next_piece
        edge_pieces.remove(next_piece)
        current_piece = next_piece
        current_matches = matches[current_piece]
        current_row += 1
    next_corner = [x[0] for x in current_matches if x[0] in corner_pieces][0]
    solved_puzzle[current_row][-1] = next_corner
    corner_pieces.remove(next_corner)
    current_piece = next_corner
    current_matches = matches[current_piece]

    # Solve the bottom edge
    current_column = -2
    while not any(x[0] in corner_pieces for x in current_matches):
        next_piece = [x[0] for x in current_matches if x[0] in edge_pieces][0]
        solved_puzzle[-1][current_column] = next_piece
        edge_pieces.remove(next_piece)
        current_piece = next_piece
        current_matches = matches[current_piece]
        current_column -= 1
    next_corner = [x[0] for x in current_matches if x[0] in corner_pieces][0]
    solved_puzzle[-1][0] = next_corner
    corner_pieces.remove(next_corner)
    current_piece = next_corner
    current_matches = matches[current_piece]

    # Solve the last edge
    current_row = -2
    while not any(x[0] == solved_puzzle[0][0] for x in current_matches):
        next_piece = [x[0] for x in current_matches if x[0] in edge_pieces][0]
        solved_puzzle[current_row][0] = next_piece
        edge_pieces.remove(next_piece)
        current_piece = next_piece
        current_matches = matches[current_piece]
        current_row -= 1

    # Solve the rest of the puzzle
    for i in range(1, len(solved_puzzle) - 1):
        for j in range(1, len(solved_puzzle[0]) - 1):
            top = solved_puzzle[i-1][j]
            left = solved_puzzle[i][j-1]
            for t in middle_pieces:
                t_matches = [x[0] for x in matches[t]]
                if top in t_matches and left in t_matches:
                    solved_puzzle[i][j] = t
                    middle_pieces.remove(t)
                    break

    # Correctly orient the top left tile
    current_piece = solved_puzzle[0][0]
    current_matches = matches[current_piece]
    right_match = [x for x in current_matches if x[0] == solved_puzzle[0][1] and x[2] < 4][0]
    bottom_match = [x for x in current_matches if x[0] == solved_puzzle[1][0] and x[2] < 4][0]

    # Rotate it so that bottom match is on bottom
    pos = bottom_match[2]
    while pos != 2:
        tiles[current_piece] = rotate(tiles[current_piece])
        pos = (pos + 1) % 4

    # Flip it horizontally if we need to
    if bottom_match[2] != (right_match[2] + 1) % 4:
        tiles[current_piece] = flip(tiles[current_piece])

    # Solve the puzzle
    for i in range(0, len(solved_puzzle)):
        if i != 0:
            # Solve the left edge of the row
            current_piece = solved_puzzle[i][0]
            current_matches = matches[current_piece]

            top_piece_bottom_edge = tiles[solved_puzzle[i-1][0]][-1]

            c = 0
            while tiles[current_piece][0] != top_piece_bottom_edge:
                tiles[current_piece] = rotate(tiles[current_piece])
                if c == 3:
                    tiles[current_piece] = flip(tiles[current_piece])
                c += 1

        # Solve each member of the row
        for j in range(1, len(solved_puzzle[0])):
            current_piece = solved_puzzle[i][j]
            current_matches = matches[current_piece]

            left_piece_right_edge = "".join([x[-1] for x in tiles[solved_puzzle[i][j-1]]])

            # rotate/flip until it works
            c = 0
            while "".join([x[0] for x in tiles[current_piece]]) != left_piece_right_edge:
                tiles[current_piece] = rotate(tiles[current_piece])
                if c == 3:
                    tiles[current_piece] = flip(tiles[current_piece])
                c += 1

    # Strip the border from the tiles
    for t in tiles:
        tiles[t] = [x[1:-1] for x in tiles[t]][1:-1]

    # Get the full puzzle image
    tile_length = len(tiles[solved_puzzle[0][0]])
    full_image = ["" for _ in range(len(solved_puzzle) * tile_length)]
    for i in range(len(solved_puzzle)):
        for j in range(len(solved_puzzle)):
            current_piece = solved_puzzle[i][j]
            current_image = tiles[current_piece]

            for k in range(0, tile_length):
                full_image[i * tile_length + k] += current_image[k]

    monster_locations = []
    rounds = 0

    monster_offsets = ((0, 18), \
                      (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), \
                      (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16))
    while len(monster_locations) == 0:
        for i in range(len(full_image) - 2):
            for j in range(len(full_image[0]) - 19):
                if all(full_image[i+i_offset][j+j_offset] == "#" for (i_offset, j_offset) in monster_offsets):
                    monster_locations.append((i, j))

        if len(monster_locations) != 0:
            break

        if rounds == 3:
            full_image = flip(full_image)
        full_image = rotate(full_image)

        rounds += 1

    full_image = [[c for c in x] for x in full_image]

    for (i, j) in monster_locations:
        for (i_offset, j_offset) in monster_offsets:
            full_image[i+i_offset][j+j_offset] = "O"

    for i in range(len(full_image)):
        full_image[i] = "".join(full_image[i])

    count = 0
    for row in full_image:
        for c in row:
            if c == "#":
                count += 1
    print(count)

def rotate(tile):
    new_tile = [["" for _ in range(len(tile[0]))] for _ in range(len(tile))]
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            new_tile[j][len(tile) - 1 - i] = tile[i][j]
    new_tile = ["".join(x) for x in new_tile]

    return new_tile


def flip(tile):
    return [x[::-1] for x in tile]

solution_part2()
