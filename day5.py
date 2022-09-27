import math

def solution_part1():
    with open('inputs/day5.txt', 'r') as f:
        max_id = 0
        for line in f:
            min = 0
            max = 127
            for c in line[:7]:
                if c == "F":
                    max = math.floor((max - min) / 2) + min
                elif c == "B":
                    min = math.ceil((max - min) / 2) + min
            row = max
            min = 0
            max = 7
            for c in line[7:10]:
                if c == "L":
                    max = math.floor((max - min) / 2) + min
                elif c == "R":
                    min = math.ceil((max - min) / 2) + min
            col = max
            seat_id = row * 8 + col
            if seat_id > max_id:
                max_id = seat_id
        print(max_id)

def solution_part2():
    with open('inputs/day5.txt', 'r') as f:
        seats = []
        for line in f:
            min = 0
            max = 127
            for c in line[:7]:
                if c == "F":
                    max = math.floor((max - min) / 2) + min
                elif c == "B":
                    min = math.ceil((max - min) / 2) + min
            row = max
            min = 0
            max = 7
            for c in line[7:10]:
                if c == "L":
                    max = math.floor((max - min) / 2) + min
                elif c == "R":
                    min = math.ceil((max - min) / 2) + min
            col = max
            seat_id = row * 8 + col
            seats.append(seat_id)
        seats.sort()
        for i in range(len(seats)):
            if seats[i + 1] != seats[i] + 1:
                print(seats[i] + 1)
                break


solution_part2()
