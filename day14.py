def solution_part1():
    with open('inputs/day14.txt', 'r') as f:
        mem = {}
        for line in f:
            sp = line.split()
            if (sp[0] == "mask"):
                mask_str = sp[-1]
                mask = {}
                for i in range(36):
                    if mask_str[i] != "X":
                        mask[i] = mask_str[i]
                continue

            bin_num = list(bin(int(sp[-1]))[2:].zfill(36))
            for i in mask:
                bin_num[i] = mask[i]

            addr = int(sp[0][4:-1])
            mem[addr] = int("".join(bin_num), 2)

        print(sum(mem.values()))


def solution_part2():
    with open('inputs/day14.txt', 'r') as f:
        mem = {}
        for line in f:
            sp = line.split()
            if (sp[0] == "mask"):
                mask = sp[-1]
                continue

            val = int(sp[-1])
            bin_addr = list(bin(int(sp[0][4:-1]))[2:].zfill(36))

            for i in range(len(mask)):
                if mask[i] != "0":
                    bin_addr[i] = mask[i]

            possible_addrs = [bin_addr]

            while "X" in possible_addrs[0]:
                x_location = possible_addrs[0].index("X")
                new_addrs = []
                for addr in possible_addrs:
                    cop1 = [x for x in addr]
                    cop2 = [x for x in addr]
                    cop1[x_location] = "0"
                    cop2[x_location] = "1"
                    new_addrs.append(cop1)
                    new_addrs.append(cop2)
                possible_addrs = new_addrs

            for addr in [int("".join(x), 2) for x in possible_addrs]:
                mem[addr] = val

        print(sum(mem.values()))

solution_part2()
