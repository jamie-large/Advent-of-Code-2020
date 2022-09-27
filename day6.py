def solution_part1():
    with open('inputs/day6.txt', 'r') as f:
        total = 0
        seen = [False] * 26
        for line in f:
            if len(line) == 1:
                total += sum(seen)
                seen = [False] * 26
                continue
            for c in line[:-1]:
                seen[ord(c) - 97] = True
        total += sum(seen)
        print(total)


def solution_part2():
    with open('inputs/day6.txt', 'r') as f:
        total = 0
        group_seen = [False] * 26
        first = True
        for line in f:
            individual_seen = [False] * 26

            if len(line) == 1:
                total += sum(group_seen)
                group_seen = [False] * 26
                first = True
                continue

            for c in line[:-1]:
                if first:
                    group_seen[ord(c) - 97] = True
                individual_seen[ord(c) - 97] = True

            for i in range(26):
                group_seen[i] = group_seen[i] and individual_seen[i]

            first = False

        total += sum(group_seen)
        print(total)


solution_part2()
