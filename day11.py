def solution_part1():
    with open("inputs/day11.txt", "r") as f:
        grid = [["."] + [c for c in x[:-1]] + ["."] for x in f.readlines()]
        grid.insert(0, ["." for _ in range(len(grid[0]))])
        grid.append(["." for _ in range(len(grid[0]))])

        next_grid = get_next_grid(grid)

        while grid != next_grid:
            grid = next_grid
            next_grid = get_next_grid(grid)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "#":
                    count += 1
        print(count)



OFFSETS = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]

def get_next_grid(grid, part=1):
    new_grid = [[c for c in x] for x in grid]
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0]) - 1):
            if part == 1:
                # If seat is empty and no occupied seats adjacent to it, it becomes occupied
                if grid[i][j] == "L" and all(grid[i+i_offset][j+j_offset] != "#" for (i_offset, j_offset) in OFFSETS):
                    new_grid[i][j] = "#"
                # If seat is occupied and four or more seats adjacent to it are occupied, it becomes empty
                elif grid[i][j] == "#" and [grid[i+i_offset][j+j_offset] == "#" for (i_offset, j_offset) in OFFSETS].count(True) >= 4:
                    new_grid[i][j] = "L"
            elif part == 2:
                if grid[i][j] == "L" and look_around(grid, i, j, "#") == 0:
                    new_grid[i][j] = "#"
                elif grid[i][j] == "#" and look_around(grid, i, j, "#") >= 5:
                    new_grid[i][j] = "L"

    return new_grid

def look_around(grid, i, j, char):
    count = 0
    # Check to the left
    c1 = j - 1
    while c1 >= 0 and c1 < len(grid[i]):
        if grid[i][c1] == char:
            count += 1
            break
        elif grid[i][c1] != ".":
            break
        c1 -= 1
    # Check to the right
    c1 = j + 1
    while c1 >= 0 and c1 < len(grid[i]):
        if grid[i][c1] == char:
            count += 1
            break
        elif grid[i][c1] != ".":
            break
        c1 += 1
    # Check above
    c1 = i - 1
    while c1 >= 0 and c1 < len(grid):
        if grid[c1][j] == char:
            count += 1
            break
        elif grid[c1][j] != ".":
            break
        c1 -= 1
    # Check below
    c1 = i + 1
    while c1 >= 0 and c1 < len(grid):
        if grid[c1][j] == char:
            count += 1
            break
        elif grid[c1][j] != ".":
            break
        c1 += 1
    # Check diagonal up left
    c1 = i - 1
    c2 = j - 1
    while c1 >= 0 and c1 < len(grid) and c2 >= 0 and c2 < len(grid[i]):
        if grid[c1][c2] == char:
            count += 1
            break
        elif grid[c1][c2] != ".":
            break
        c1 -= 1
        c2 -= 1
    # Check diagonal up right
    c1 = i - 1
    c2 = j + 1
    while c1 >= 0 and c1 < len(grid) and c2 >= 0 and c2 < len(grid[i]):
        if grid[c1][c2] == char:
            count += 1
            break
        elif grid[c1][c2] != ".":
            break
        c1 -= 1
        c2 += 1
    # Check diagonal down left
    c1 = i + 1
    c2 = j - 1
    while c1 >= 0 and c1 < len(grid) and c2 >= 0 and c2 < len(grid[i]):
        if grid[c1][c2] == char:
            count += 1
            break
        elif grid[c1][c2] != ".":
            break
        c1 += 1
        c2 -= 1
    # Check diagonal down right
    c1 = i + 1
    c2 = j + 1
    while c1 >= 0 and c1 < len(grid) and c2 >= 0 and c2 < len(grid[i]):
        if grid[c1][c2] == char:
            count += 1
            break
        elif grid[c1][c2] != ".":
            break
        c1 += 1
        c2 += 1
    return count


def solution_part2():
    with open("inputs/day11.txt", "r") as f:
        grid = [["."] + [c for c in x[:-1]] + ["."] for x in f.readlines()]
        grid.insert(0, ["." for _ in range(len(grid[0]))])
        grid.append(["." for _ in range(len(grid[0]))])

        next_grid = get_next_grid(grid)

        while grid != next_grid:
            grid = next_grid
            next_grid = get_next_grid(grid, part=2)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "#":
                    count += 1
        print(count)

solution_part2()
