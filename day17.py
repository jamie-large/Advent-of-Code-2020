def solution_part1():
    with open('inputs/day17.txt', 'r') as f:
        grid = [[[c for c in word[:-1]] for word in f.readlines()]]
        for _ in range(6):
            grid = calculate_grid(grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for k in range(len(grid[0][0])):
                    if grid[i][j][k] == "#":
                        count += 1
        print(count)

def calculate_grid(grid):
    expanded_grid = expand_grid(grid)
    new_grid = expand_grid(grid)
    for i in range(len(expanded_grid)):
        for j in range(len(expanded_grid[0])):
            for k in range(len(expanded_grid[0][0])):
                active_neighbors = count_active_neighbors(expanded_grid, i, j, k)
                if expanded_grid[i][j][k] == "#":
                    if active_neighbors != 2 and active_neighbors != 3:
                        new_grid[i][j][k] = "."
                elif expanded_grid[i][j][k] == ".":
                    if active_neighbors == 3:
                        new_grid[i][j][k] = "#"
    return new_grid


def count_active_neighbors(grid, x, y, z):
    x += 1
    y += 1
    z += 1
    expanded_grid = expand_grid(grid)
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if (i != x or j != y or k != z) and (expanded_grid[i][j][k] == "#"):
                    count += 1
                    if count >= 4:
                        return count
    return count

def expand_grid(grid):
    new_grid = [[["."] * (len(grid[0]) + 2) for _ in range(len(grid[0]) + 2)]]
    for s in grid:
        new_grid.append(expand_slice(s))
    new_grid.append([["."] * (len(grid[0]) + 2) for _ in range(len(grid[0]) + 2)])
    return new_grid

def expand_slice(s):
    new_slice = [["."] * (len(s[0]) + 2)]
    for row in s:
        new_slice.append(["."] + row + ["."])
    new_slice.append(["."] * (len(s[0]) + 2))
    return new_slice

def solution_part2():
    with open('inputs/day17.txt', 'r') as f:
        space = [[[[c for c in word[:-1]] for word in f.readlines()]]]
        for i in range(6):
            space = calculate_space(space)
        count = 0
        for i in range(len(space)):
            for j in range(len(space[0])):
                for k in range(len(space[0][0])):
                    for l in range(len(space[0][0][0])):
                        if space[i][j][k][l] == "#":
                            count += 1
        print(count)


def expand_space(space):
    new_space = [[[["."] * (len(space[0][0][0]) + 2) for _ in range(len(space[0][0]) + 2)] for _ in range(len(space[0]) + 2)]]
    for grid in space:
        new_space.append(expand_grid(grid))
    new_space.append([[["."] * (len(space[0][0][0]) + 2) for _ in range(len(space[0][0]) + 2)] for _ in range(len(space[0]) + 2)])
    return new_space

def calculate_space(space):
    expanded_space = expand_space(space)
    new_space = expand_space(space)
    for i in range(len(expanded_space)):
        for j in range(len(expanded_space[0])):
            for k in range(len(expanded_space[0][0])):
                for l in range(len(expanded_space[0][0][0])):
                    active_neighbors = count_active_neighbors_space(expanded_space, i, j, k, l)
                    if expanded_space[i][j][k][l] == "#":
                        if active_neighbors != 2 and active_neighbors != 3:
                            new_space[i][j][k][l] = "."
                    elif expanded_space[i][j][k][l] == ".":
                        if active_neighbors == 3:
                            new_space[i][j][k][l] = "#"
    return new_space

def count_active_neighbors_space(space, x, y, z, w):
    x += 1
    y += 1
    z += 1
    w += 1
    expanded_space = expand_space(space)
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if (i != x or j != y or k != z or l != w) and (expanded_space[i][j][k][l] == "#"):
                        count += 1
                        if count >= 4:
                            return count
    return count

solution_part2()
