def solution_part1():
    with open('inputs/day4.txt', 'r') as f:
        count = 0
        values = { "byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": True}
        for line in f:
            if len(line) > 1:
                words = [x[:3] for x in line.split()]
                for word in words:
                    values[word] = True
            else:
                for v in values.values():
                    if v == False:
                        break
                else:
                    count += 1
                values = { "byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": True}
        for v in values.values():
            if v == False:
                break
        else:
            count += 1

        print(count)

def solution_part2():
    with open('inputs/day4.txt', 'r') as f:
        count = 0
        values = { "byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": True}
        invalid = False
        for line in f:
            if len(line) > 1:
                words = [(x[:3], x[4:]) for x in line.split()]
                for field, val in words:
                    values[field] = True
                    if field == "byr":
                        if len(val) != 4 or not val.isnumeric() or int(val) < 1920 or int(val) > 2002:
                            invalid = True
                    elif field == "iyr":
                        if len(val) != 4 or not val.isnumeric() or int(val) < 2010 or int(val) > 2020:
                            invalid = True
                    elif field == "eyr":
                        if len(val) != 4 or not val.isnumeric() or int(val) < 2020 or int(val) > 2030:
                            invalid = True
                    elif field == "hgt":
                        if len(val) <= 2:
                            invalid = True
                            continue
                        unit = val[-2:]
                        val = val[:-2]
                        if val.isnumeric() and unit == "cm":
                            if int(val) < 150 or int(val) > 193:
                                invalid = True
                        elif val.isnumeric() and unit == "in":
                            if int(val) < 59 or int(val) > 76:
                                invalid = True
                        else:
                            invalid = True
                    elif field == "hcl":
                        if len(val) != 7 or val[0] != "#":
                            invalid = True
                        for c in val[1:]:
                            if c not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"):
                                invalid = True
                    elif field == "ecl":
                        if len(val) != 3 or val not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                            invalid = True
                    elif field == "pid":
                        if len(val) != 9 or not val.isnumeric():
                            invalid = True
            else:
                for v in values.values():
                    if invalid or v == False:
                        break
                else:
                    count += 1
                values = { "byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": True}
                invalid = False
        for v in values.values():
            if invalid or v == False:
                break
        else:
            count += 1

        print(count)

solution_part2()
