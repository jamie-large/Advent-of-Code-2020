def solution_part1():
    with open('inputs/day3.txt', 'r') as f:
        treeMap = [[c for c in line[:-1]] for line in f]
        count = 0
        row = 0
        col = 0
        while row < len(treeMap):
            if treeMap[row][col] == '#':
                count += 1
            row += 1
            col = (col + 3) % len(treeMap[0])

        print(count)

def solution_part2():
    with open('inputs/day3.txt', 'r') as f:
        treeMap = [[c for c in line[:-1]] for line in f]
        value = 1
        for (right, down) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
            count = 0
            row = 0
            col = 0
            while row < len(treeMap):
                if treeMap[row][col] == '#':
                    count += 1
                row += down
                col = (col + right) % len(treeMap[0])

            print(count)
            value *= count
        print(value)

solution_part2()
