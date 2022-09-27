def solution_part1():
    with open("inputs/day22.txt", "r") as f:
        decks = [[], []]
        player = 0
        for line in f:
            if len(line) == 1:
                player += 1
            try:
                val = int(line)
                decks[player].append(val)
            except:
                continue

        while not any(len(d) == 0 for d in decks):
            if decks[0][0] > decks[1][0]:
                decks[0].append(decks[0].pop(0))
                decks[0].append(decks[1].pop(0))
            else:
                decks[1].append(decks[1].pop(0))
                decks[1].append(decks[0].pop(0))


        winner = 0 if len(decks[0]) > 0 else 1
        value = 0
        for i in range(len(decks[winner])):
            value += (len(decks[winner]) - i) * decks[winner][i]

        print(value)

def solution_part2():
    with open("inputs/day22.txt", "r") as f:
        decks = [[], []]
        player = 0
        for line in f:
            if len(line) == 1:
                player += 1
            try:
                val = int(line)
                decks[player].append(val)
            except:
                continue

        winner, decks = play_game(decks)
        value = 0
        for i in range(len(decks[winner])):
            value += (len(decks[winner]) - i) * decks[winner][i]

        print(value)


WINS_CACHE = {}

def play_game(decks):
    seen_decks = set()
    winner = -1
    while not any(len(d) == 0 for d in decks):
        decks_str = str(decks)
        if decks_str in WINS_CACHE:
            for sd in seen_decks:
                WINS_CACHE[sd] = WINS_CACHE[decks_str]
            return WINS_CACHE[decks_str]
        if decks_str in seen_decks:
            for sd in seen_decks:
                WINS_CACHE[sd] = (0, decks)
            return 0, decks
        seen_decks.add(decks_str)
        round_winner = -1
        if all(d[0] <= len(d) - 1 for d in decks):
            round_winner, _ = play_game([[x for x in d[1:d[0]+1]] for d in decks])
        else:
            round_winner = 0 if decks[0][0] > decks[1][0] else 1
        round_loser = (round_winner + 1) % 2
        decks[round_winner].append(decks[round_winner].pop(0))
        decks[round_winner].append(decks[round_loser].pop(0))

    winner = 0 if len(decks[0]) > 0 else 1
    for sd in seen_decks:
        WINS_CACHE[sd] = (winner, decks)
    return winner, decks

solution_part2()
