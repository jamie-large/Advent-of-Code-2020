def solution_part1():
    with open('inputs/day15.txt', 'r') as f:
        starting_nums = [int(x) for x in f.readline().split(",")]
        history = {}
        for i in range(len(starting_nums) - 1):
            history[starting_nums[i]] = i + 1

        most_recent = starting_nums[-1]
        round = len(starting_nums) + 1
        while round <= 2020:
            val = 0 if most_recent not in history else round - history[most_recent] - 1

            history[most_recent] = round - 1
            most_recent = val

            round += 1

        print(most_recent)



def solution_part2():
    with open('inputs/day15.txt', 'r') as f:
        starting_nums = [int(x) for x in f.readline().split(",")]
        history = {}
        for i in range(len(starting_nums) - 1):
            history[starting_nums[i]] = i + 1

        most_recent = starting_nums[-1]
        round = len(starting_nums) + 1
        while round <= 30000000:
            val = 0 if most_recent not in history else round - history[most_recent] - 1

            history[most_recent] = round - 1
            most_recent = val

            round += 1

        print(most_recent)

solution_part2()







