CARDINAL_DIRECTIONS = ["N", "E", "S", "W"]
def solution_part1():
    with open("inputs/day12.txt", "r") as f:
        position = [0,0]
        direction = "E"
        for line in f:
            dir = line[0]
            units = int(line[1:])
            if dir == "R":
                while units != 0:
                    direction = CARDINAL_DIRECTIONS[(CARDINAL_DIRECTIONS.index(direction) + 1) % 4]
                    units -= 90
                continue
            if dir == "L":
                while units != 0:
                    direction = CARDINAL_DIRECTIONS[CARDINAL_DIRECTIONS.index(direction) - 1]
                    units -= 90
                continue

            if dir == "F":
                dir = direction

            if dir == "N":
                position[1] += units
            elif dir == "S":
                position[1] -= units
            elif dir == "E":
                position[0] += units
            elif dir == "W":
                position[0] -= units

        print(abs(position[0]) + abs(position[1]))

def solution_part2():
    with open("inputs/day12.txt", "r") as f:
        ship_position = [0,0]
        waypoint_position = [10,1]
        for line in f:
            dir = line[0]
            units = int(line[1:])
            if dir == "R":
                while units != 0:
                    waypoint_position = [waypoint_position[1], waypoint_position[0] * -1]
                    units -= 90
            elif dir == "L":
                while units != 0:
                    waypoint_position = [waypoint_position[1] * -1, waypoint_position[0]]
                    units -= 90
            elif dir == "F":
                ship_position[0] += waypoint_position[0] * units
                ship_position[1] += waypoint_position[1] * units
            elif dir == "N":
                waypoint_position[1] += units
            elif dir == "S":
                waypoint_position[1] -= units
            elif dir == "E":
                waypoint_position[0] += units
            elif dir == "W":
                waypoint_position[0] -= units

        print(abs(ship_position[0]) + abs(ship_position[1]))

solution_part2()
