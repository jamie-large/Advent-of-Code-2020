def solution_part1():
    with open('inputs/day19.txt', 'r') as f:
        rules = {}
        inputs = []
        state = 0
        for line in f:
            if state == 0:
                if len(line) == 1:
                    state = 1
                    continue
                sp = line[:-1].split(":")
                if sp[1][1] == '"':
                    rules[int(sp[0])] = sp[1][2]
                else:
                    rules[int(sp[0])] = [[int(s) for s in p.split()] for p in sp[1].split("|")]
            if state == 1:
                inputs.append(line[:-1])

        all_valid = {}
        for valid_input in generate_valid(rules, 0):
            all_valid[valid_input] = True

        count = 0
        for i in inputs:
            if i in all_valid:
                count += 1
        print(count)


solved = {}
def generate_valid(rules, current):
    # base-case: already solved
    if current in solved:
        return solved[current]
    # base-case: simple rule
    if rules[current] == "a" or rules[current] == "b":
        solved[current] = [rules[current]]
        return solved[current]

    valid = []
    # Otherwise, figure out all valid strings
    for sequence in rules[current]:
        valid_sequence = [generate_valid(rules, i) for i in sequence]
        while len(valid_sequence) > 1:
            valid_sequence[0] = combine_valid(valid_sequence[0], valid_sequence[1])
            valid_sequence.pop(1)
        valid = valid + valid_sequence[0]

    solved[current] = valid
    return valid

def combine_valid(val1, val2):
    result = []
    for i in val1:
        for j in val2:
            result.append(i + j)
    return result


def solution_part2():
    with open('inputs/day19.txt', 'r') as f:
        rules = {}
        inputs = []
        state = 0
        for line in f:
            if state == 0:
                if len(line) == 1:
                    state = 1
                    continue
                sp = line[:-1].split(":")
                if sp[1][1] == '"':
                    rules[int(sp[0])] = sp[1][2]
                else:
                    rules[int(sp[0])] = [[int(s) for s in p.split()] for p in sp[1].split("|")]
            if state == 1:
                inputs.append(line[:-1])

        valid_42 = generate_valid(rules, 42)
        valid_31 = generate_valid(rules, 31)

        word_length = len(valid_42[0])

        count = 0
        for inp in inputs:
            # See if it can be made by (42) * n + (31) * m, where n > m
            count_42 = 0
            c = 0
            while c + word_length <= len(inp):
                if inp[c:c+word_length] in valid_42:
                    c += word_length
                    count_42 += 1
                else:
                    break
            count_31 = 0
            while c + word_length <= len(inp):
                if inp[c:c+word_length] in valid_31:
                    c += word_length
                    count_31 += 1
                else:
                    break
            if c == len(inp) and count_31 > 0 and count_42 > count_31:
                count += 1

        print(count)

solution_part2()
