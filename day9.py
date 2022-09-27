from sortedcontainers import SortedSet

def solution_part1():
    with open('inputs/day9.txt', 'r') as f:
        inp = [int(line) for line in f.readlines()]
        size_limit = 25
        seen_numbers = SortedSet()
        for i in range(size_limit):
            seen_numbers.add(inp[i])
        for i in range(size_limit, len(inp)):
            current_number = inp[i]
            valid = False
            for sn in seen_numbers:
                if current_number - sn in seen_numbers:
                    valid = True
                    break
                if sn > current_number / 2:
                    break
            if not valid:
                print(current_number)
                return current_number

            seen_numbers.remove(inp[i - size_limit])
            seen_numbers.add(current_number)



def solution_part2():
    with open('inputs/day9.txt', 'r') as f:
        inp = [int(line) for line in f.readlines()]
        target_value = solution_part1()
        buffer = []
        current_sum = 0

        for i in inp:
            current_sum += i
            buffer.append(i)
            while current_sum > target_value:
                current_sum -= buffer[0]
                buffer.pop(0)
            if current_sum == target_value:
                print(min(buffer) + max(buffer))
                return

solution_part2()
