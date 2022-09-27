def solution_part1():
    with open('inputs/day10.txt', 'r') as f:
        nums = [int(x) for x in f.readlines()]
        nums.append(0)
        nums.sort()
        nums.append(nums[-1] + 3)

        total_1 = 0
        total_3 = 0
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                total_1 += 1
            elif nums[i+1] - nums[i] == 3:
                total_3 += 1

        print(total_1 * total_3)


def solution_part2():
    with open('inputs/day10.txt', 'r') as f:
        nums = [int(x) for x in f.readlines()]
        nums.append(0)
        nums.sort()
        nums.append(nums[-1] + 3)

        total_configs = [-1] * len(nums)
        total_configs[-1] = 1

        print(solve(total_configs, nums, 0))

def solve(total_configs, nums, current):
    if total_configs[current] != -1:
        return total_configs[current]
    value = 0
    if (current + 1 < len(nums) and nums[current + 1] - nums[current] <= 3):
        value += solve(total_configs, nums, current + 1)
    if (current + 2 < len(nums) and nums[current + 2] - nums[current] <= 3):
        value += solve(total_configs, nums, current + 2)
    if (current + 3 < len(nums) and nums[current + 3] - nums[current] <= 3):
        value += solve(total_configs, nums, current + 3)
    total_configs[current] = value
    return value


solution_part2()
