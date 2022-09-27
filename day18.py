def solution_part1():
    with open('inputs/day18.txt', 'r') as f:
        sum = 0
        for line in f:
            sum += int(solve_expression(line[:-1]))
        print(sum)

def solve_expression(exp, part=1):
    # If there are parentheses, solve that expression first
    open_index = exp.find("(")
    while open_index > -1:
        c = open_index + 1
        count = 1
        while count != 0:
            if exp[c] == ")":
                count -= 1
            elif exp[c] == "(":
                count += 1
            c += 1

        exp = exp[:open_index] + solve_expression(exp[open_index + 1:c-1], part) + exp[c:]
        open_index = exp.find("(")

    if part == 2:
        sp = exp.split("+", 1)
        while len(sp) == 2:
            left_sp = sp[0].split()
            right_sp = sp[1].split()
            exp = " ".join(left_sp[:-1]) + " " + str(int(left_sp[-1]) + int(right_sp[0])) + " " + " ".join(right_sp[1:])
            sp = exp.split("+", 1)


    sp = exp.strip().split(" ", 3)

    if len(sp) == 1:
        return sp[0]

    new_value = int(sp[0]) + int(sp[2]) if sp[1] == "+" else int(sp[0]) * int(sp[2])

    while len(sp) != 3:
        exp = str(new_value) + " " + sp[3]
        sp = exp.strip().split(" ", 3)
        new_value = int(sp[0]) + int(sp[2]) if sp[1] == "+" else int(sp[0]) * int(sp[2])

    return str(new_value)

def solution_part2():
    with open('inputs/day18.txt', 'r') as f:
        sum = 0
        for line in f:
            sum += int(solve_expression(line[:-1], 2))
        print(sum)

solution_part2()
