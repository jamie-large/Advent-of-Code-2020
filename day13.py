def solution_part1():
    with open("inputs/day13.txt", "r") as f:
        original_time = int(f.readline()[:-1])
        departure_time = original_time
        buses = [int(x) for x in f.readline().split(",") if x != "x"]

        while True:
            for bus in buses:
                if departure_time % bus == 0:
                    print(bus * (departure_time - original_time))
                    return
            departure_time += 1



def solution_part2():
    with open("inputs/day13.txt", "r") as f:
        buses = [int(x) if x != "x" else x for x in f.readlines()[1].split(",")]

        t = buses[0]
        c = buses[0]
        i = 1
        while(buses[i] == "x"):
            i += 1
        iter = 0
        while True:
            iter += 1
            if (t + i) % buses[i] == 0:
                c = c * buses[i]
                i += 1

                while i < len(buses) and buses[i] == "x":
                    i += 1

                if i == len(buses):
                    break

                continue
            t += c
        print(t)
        print(iter)

solution_part2()
