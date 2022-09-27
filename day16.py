from sortedcontainers import SortedSet

def solution_part1():
    with open('inputs/day16.txt', 'r') as f:
        valid = [False] * 1000
        stage = 0
        total = 0
        for line in f:
            if len(line) == 1:
                continue
            if stage == 0:
                if line == "your ticket:\n":
                    stage = 1
                    continue
                ranges = [ran.strip().split("-") for ran in line.split(":")[1].split("or")]
                for r in ranges:
                    [low, high] = [int(x) for x in r]
                    for i in range(low, high + 1):
                        valid[i] = True
            elif stage == 1:
                if line == "nearby tickets:\n":
                    stage = 2
                    continue
            elif stage == 2:

                nums = [int(n) for n in line.split(",")]
                for n in nums:
                    if not valid[n]:
                        total += n
        print(total)

def DFS_SOLVE(possibilities_map):
    # Figure out which term has the least number of possibilities
    min_poss = 100000
    min_index = None
    for p in range(len(possibilities_map)):
        if len(possibilities_map[p]) < min_poss and len(possibilities_map[p]) > 1:
            min_poss = len(possibilities_map[p])
            min_index = p

    # Assign each possibility
    for possibility in possibilities_map[min_index]:
        new_map = [[x for x in p] for p in possibilities_map]
        new_map[min_index] = [possibility]

        # Remove this possibility from each other possibility map
        for i in range(len(new_map)):
            if i != min_index and possibility in new_map[i]:
                new_map[i].remove(possibility)

        # Check if impossible
        if any(len(x) == 0 for x in new_map):
            continue

        # Check if solved
        if all(len(x) == 1 for x in new_map):
            return new_map

        solution = DFS_SOLVE(new_map)
        if solution:
            return solution

    return False


def solution_part2():
    with open('inputs/day16.txt', 'r') as f:
        valid = [False] * 1000
        stage = 0
        rules = {}
        your_ticket = []
        all_tickets = []
        for line in f:
            if len(line) == 1:
                continue
            if stage == 0:
                if line == "your ticket:\n":
                    stage = 1
                    continue
                [name, rule] = line.split(":")
                rules[name] = []
                ranges = [ran.strip().split("-") for ran in rule.split("or")]
                for r in ranges:
                    [low, high] = [int(x) for x in r]
                    for i in range(low, high + 1):
                        valid[i] = True
                    rules[name].append((low, high))
            elif stage == 1:
                if line == "nearby tickets:\n":
                    stage = 2
                    continue
                your_ticket = [int(x) for x in line.split(",")]
            elif stage == 2:
                current_ticket = [int(n) for n in line.split(",")]
                if all(valid[n] for n in current_ticket):
                    all_tickets.append(current_ticket)

        possibilities_map = [[] for _ in range(len(all_tickets[0]))]

        # Get all the values for an unsolved index
        for i in list(range(len(all_tickets[0]))):
            all_values = [ticket[i] for ticket in all_tickets]
            possible_rules = list(rules.keys())
            for pr in list(rules.keys()):
                valid_ranges = rules[pr]
                if not all((value >= valid_ranges[0][0] and value <= valid_ranges[0][1]) or \
                            (value >= valid_ranges[1][0] and value <= valid_ranges[1][1])  for value in all_values):
                    possible_rules.remove(pr)
            possibilities_map[i] = possible_rules

        solution = [x[0] for x in DFS_SOLVE(possibilities_map)]

        value = 1
        for i in range(len(solution)):
            if solution[i].split()[0] == "departure":
                value *= your_ticket[i]

        print(value)



solution_part2()







