def solution_part1():
    with open('inputs/day2.txt', 'r') as f:
        valid = 0
        for line in f:
            [nRange, letter, password] = line.split(' ')
            letter = letter[0]
            [low, high] = [int(x) for x in nRange.split('-')]
            letterCount = 0
            for c in password:
                if c == letter:
                    letterCount += 1
                if letterCount > high:
                    break
            if letterCount >= low and letterCount <= high:
                valid += 1
        print(valid)

def solution_part2():
    with open('inputs/day2.txt', 'r') as f:
        valid = 0
        for line in f:
            [nRange, letter, password] = line.split(' ')
            letter = letter[0]
            [low, high] = [int(x) for x in nRange.split('-')]
            count = 0
            if low - 1 < len(password) and password[low - 1] == letter:
                count += 1
            if high - 1 < len(password) and password[high - 1] == letter:
                count += 1
            if count == 1:
                valid += 1

        print(valid)

solution_part2()
