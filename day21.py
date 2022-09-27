def solution_part1():
    with open("inputs/day21.txt", "r") as f:
        rules = []
        ingredients_map = {}
        allergens_map = {}
        for line in f:
            [ingredients, allergens] = [x.split() for x in line.split("(")]
            allergens = [x[:-1] for x in allergens[1:]]
            for ingredient in ingredients:
                if ingredient not in ingredients_map:
                    ingredients_map[ingredient] = set()
                for allergen in allergens:
                    ingredients_map[ingredient].add(allergen)
            for allergen in allergens:
                if allergen not in allergens_map:
                    allergens_map[allergen] = set()
                for ingredient in ingredients:
                    allergens_map[allergen].add(ingredient)
            rules.append((set(ingredients), set(allergens)))

        failed_ingredients = []

        for ing in ingredients_map:
            if not any(DFS_FIND_FAILURES({alg: ing}, rules, allergens_map) for alg in ingredients_map[ing]):
                failed_ingredients.append(ing)

        count = 0
        for ing in failed_ingredients:
            for r in rules:
                if ing in r[0]:
                    count += 1
        print(count)

        return rules, ingredients_map, allergens_map, failed_ingredients

def DFS_FIND_FAILURES(current_solution, rules, allergens_map):
    solved_allergens = set(current_solution.keys())
    # If invalid solution (rule cannot be fulfilled), return False
    for r in rules:
        for a in r[1]:
            if a in solved_allergens and current_solution[a] not in r[0]:
                return False

    # If complete solution, return True
    if len(current_solution) == len(allergens_map):
        return True

    solved_ingredients = set(current_solution.values())
    # Otherwise, find all possible children. If any are true, we're good
    for a in allergens_map:
        if a in solved_allergens:
            continue
        for i in allergens_map[a]:
            if i in solved_ingredients:
                continue
            current_solution[a] = i
            if DFS_FIND_FAILURES(current_solution, rules, allergens_map):
                return True
            current_solution.pop(a)

def solution_part2():
    with open("inputs/day21.txt", "r") as f:
        # rules = []
        # ingredients_map = {}
        # allergens_map = {}
        # for line in f:
        #     [ingredients, allergens] = [x.split() for x in line.split("(")]
        #     allergens = [x[:-1] for x in allergens[1:]]
        #     for ingredient in ingredients:
        #         if ingredient not in ingredients_map:
        #             ingredients_map[ingredient] = set()
        #         for allergen in allergens:
        #             ingredients_map[ingredient].add(allergen)
        #     for allergen in allergens:
        #         if allergen not in allergens_map:
        #             allergens_map[allergen] = set()
        #         for ingredient in ingredients:
        #             allergens_map[allergen].add(ingredient)
        #     rules.append((set(ingredients), set(allergens)))

        # failed_ingredients = ['jnlgn', 'xqth', 'vhdt', 'jjhfbn', 'vvrhc', 'hbrplx', 'dtkr', 'fnlqrk', 'vvbqtz', 'prkblp', 'ffj', 'zkkz', 'vmb', 'qjg', 'sfghbs', 'srjv', 'vphhllt', 'qszsz', 'rzbncvnc', 'mfbfsz', 'xdjk', 'plxs', 'xgc', 'gfzmpxq', 'rmpfkv', 'tglj', 'rsmstv', 'lfckh', 'rkllz', 'qczmsk', 'zdpxfl', 'zfsbvl', 'mmdcl', 'nzqx', 'gzsdm', 'mqv', 'cmffmd', 'gjlql', 'htmb', 'fqrm', 'prtvmb', 'smbdlcg', 'zgzt', 'zcvs', 'qcksk', 'trpbj', 'jbslsbv', 'lhtpf', 'jgjrj', 'tqlbk', 'mgrr', 'zgdt', 'txldvd', 'tvz', 'zvrm', 'brvz', 'kzklp', 'zcxq', 'krpcn', 'rxv', 'ztpmz', 'hnngrhk', 'dqspdq', 'qmqbz', 'qpndpm', 'dfsnq', 'dktlp', 'zxnjkf', 'crjpt', 'qthxnb', 'tcflf', 'fsmqv', 'rnjlpq', 'vvnmqt', 'scnc', 'khmzbj', 'xkmz', 'lxpqkn', 'nxvzp', 'fktgv', 'rkkgm', 'hlhc', 'kzrk', 'pffccf', 'ndkmq', 'bxc', 'czzx', 'vdjtl', 'rkkpgs', 'sdggf', 'jszqhpf', 'zhbtz', 'pdst', 'qltvp', 'rbjdgh', 'nnrctqh', 'hprqd', 'tcfgv', 'jrpm', 'mnn', 'mqscmlf', 'qnc', 'vhr', 'xrvgdh', 'cqkprv', 'trjqbr', 'cqs', 'xbzns', 'mbdbf', 'frnmdqx', 'qvjk', 'srfm', 'brkds', 'lkzfc', 'tsjtr', 'dkshp', 'qrbbf', 'sxpbg', 'mvmhqbpz', 'tvdntm', 'qplx', 'btttz', 'zsd', 'vvz', 'sgn', 'tkv', 'krnfm', 'crbd', 'fnpkmh', 'qktcqv', 'hzxx', 'fvt', 'nchjqv', 'tdszhqn', 'dlzb', 'jmvv', 'ltbqt', 'ftrnplt', 'rtjbpd', 'vmq', 'nltv', 'cghkbp', 'vrgdk', 'hbjmtc', 'tftpnc', 'flxplq', 'tbnlrpb', 'qpkbc', 'qmcdlz', 'lnvrg', 'zbnv', 'zljsv', 'prpbcv', 'hxcc', 'mbx', 'nhldb', 'rzbrrr', 'vhmpqd', 'tfn', 'qvks', 'zkxxnhn', 'lzxpn', 'xzd', 'zptr', 'hxq', 'sgmsn', 'qlrxfv', 'tkrflnf', 'ftssfh', 'rbbnskn', 'rd', 'szsrnsc', 'bmpnrhb', 'jrlzcv', 'vpvm', 'rmzbr', 'fvghn', 'zqnn', 'kssgts', 'gpvcz', 'phkxp', 'znhjn', 'lsnnzp', 'tlbtr', 'tzc', 'xqszlhq', 'gjmbv', 'cvnmx', 'kstd', 'bvdqd', 'rxjsq', 'ftdbz']
        # failed_ingredients = ['kfcds', 'nhms', 'sbzzf', 'trh']
        rules, ingredients_map, allergens_map, failed_ingredients = solution_part1()

        for i in failed_ingredients:
            for r in rules:
                if i in r[0]:
                    r[0].remove(i)
            ingredients_map.pop(i)
            for a in allergens_map:
                if i in allergens_map[a]:
                    allergens_map[a].remove(i)

        solved_map = DFS_SOLVE({}, rules, allergens_map)
        all_allergens = list(allergens_map.keys())
        all_allergens.sort()
        solution = ""
        for a in all_allergens:
            solution += solved_map[a] + ","
        print(solution[:-1])

def DFS_SOLVE(current_solution, rules, allergens_map):
    solved_allergens = set(current_solution.keys())
    # If invalid solution (rule cannot be fulfilled), return False
    for r in rules:
        for a in r[1]:
            if a in solved_allergens and current_solution[a] not in r[0]:
                return False

    # If complete solution, return it
    if len(current_solution) == len(allergens_map):
        return current_solution

    solved_ingredients = set(current_solution.values())
    # Otherwise, find all possible children
    for a in allergens_map:
        if a in solved_allergens:
            continue
        for i in allergens_map[a]:
            if i in solved_ingredients:
                continue
            current_solution[a] = i
            success = DFS_SOLVE(current_solution, rules, allergens_map)
            if success:
                return success
            current_solution.pop(a)

solution_part2()
