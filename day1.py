def solution_part1():
    with open('inputs/day1.txt', 'r') as f:
        seenNumbers = [0] * 2021
        for line in f:
            current_number = int(line)
            if seenNumbers[2020 - current_number] > 0:
                print(current_number * (2020 - current_number))
                return
            seenNumbers[current_number] += 1

def solution_part2():
    with open('inputs/day1.txt', 'r') as f:
        previousValues = []
        seenNumbers = [0] * 2021
        for line in f:
            current_number = int(line)
            for previous_number in previousValues:
                if 2020 - previous_number - current_number > 0 and seenNumbers[2020 - previous_number - current_number] > 0:
                    print(current_number * previous_number * (2020 - previous_number - current_number))
                    return
            seenNumbers[current_number] += 1
            previousValues.append(current_number)

solution_part2()
