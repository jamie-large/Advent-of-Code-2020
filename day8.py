def solution_part1():
    with open('inputs/day8.txt', 'r') as f:
        program = [(words[0], int(words[1][1:]) if words[1][0] == "+" else int(words[1])) for words in [line.split() for line in f.readlines()]]
        accumulator = 0
        current_line = 0
        seen_line = [False] * len(program)
        while not seen_line[current_line]:
            seen_line[current_line] = True
            if program[current_line][0] == "acc":
                accumulator += program[current_line][1]
                current_line += 1
            elif program[current_line][0] == "jmp":
                current_line += program[current_line][1]
            elif program[current_line][0] == "nop":
                current_line += 1
        print(accumulator)


def solution_part2():
    with open('inputs/day8.txt', 'r') as f:
        program = [[words[0], int(words[1][1:]) if words[1][0] == "+" else int(words[1])] for words in [line.split() for line in f.readlines()]]
        for i in range(len(program)):
            if program[i][0] == "nop":
                program[i][0] = "jmp"
                accumulator = 0
                current_line = 0
                seen_line = [False] * len(program)
                while current_line < len(program) and not seen_line[current_line]:
                    seen_line[current_line] = True
                    if program[current_line][0] == "acc":
                        accumulator += program[current_line][1]
                        current_line += 1
                    elif program[current_line][0] == "jmp":
                        current_line += program[current_line][1]
                    elif program[current_line][0] == "nop":
                        current_line += 1
                if current_line == len(program):
                    print(accumulator)
                    return
                program[i][0] = "nop"

            elif program[i][0] == "jmp":
                program[i][0] = "nop"
                accumulator = 0
                current_line = 0
                seen_line = [False] * len(program)
                while current_line < len(program) and not seen_line[current_line]:
                    seen_line[current_line] = True
                    if program[current_line][0] == "acc":
                        accumulator += program[current_line][1]
                        current_line += 1
                    elif program[current_line][0] == "jmp":
                        current_line += program[current_line][1]
                    elif program[current_line][0] == "nop":
                        current_line += 1
                if current_line == len(program):
                    print(accumulator)
                    return
                program[i][0] = "jmp"

solution_part2()
