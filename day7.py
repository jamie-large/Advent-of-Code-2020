def solution_part1():
    with open('inputs/day7.txt', 'r') as f:
        rules = {}
        for line in f:
            [container, contained] = line.split("contain")
            container_words = container.split()
            container_color = container_words[0] + " " + container_words[1]
            contained_colors = []
            if contained[1:3] != "no":
                for contained_bag in contained.split(","):
                    contained_bag_words = contained_bag.split()
                    contained_colors.append(contained_bag_words[1] + " " + contained_bag_words[2])
            rules[container_color] = contained_colors
        count = 0
        for color in rules:
            if solve(color, rules):
                count += 1

        print(count)

solved = {}
def solve(color, rules):
    if color in solved:
        return solved[color]
    if rules[color] == []:
        solved[color] = False
        return False
    for child in rules[color]:
        if child == "shiny gold" or solve(child, rules):
            solved[color] = True
            return True
    solved[color] = False
    return False


def solution_part2():
    with open('inputs/day7.txt', 'r') as f:
        rules = {}
        for line in f:
            [container, contained] = line.split("contain")
            container_words = container.split()
            container_color = container_words[0] + " " + container_words[1]
            contained_colors = []
            if contained[1:3] != "no":
                for contained_bag in contained.split(","):
                    contained_bag_words = contained_bag.split()
                    contained_colors.append((int(contained_bag_words[0]), contained_bag_words[1] + " " + contained_bag_words[2]))
            rules[container_color] = contained_colors

        print(bags_contained("shiny gold", rules));

bags_contained_cache = {}
def bags_contained(color, rules):
    if color in bags_contained_cache:
        return bags_contained_cache[color]
    total = 0
    for child in rules[color]:
        total += child[0] * (1 + bags_contained(child[1], rules))
    bags_contained_cache[color] = total
    return total

solution_part2()
