sample = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def parse(puzz: str):
    lines = puzz.split('\n')
    parsed = {}
    for line in lines:
        if line:
            before, after = line.split(': ')
            id_ = int(before[5:])
            winners, entries = after.split(' | ')
            winners = [int(w) for w in winners.split()]
            entries = [int(e) for e in entries.split()]
            parsed.update({id_: (winners, entries)})
    return parsed

def score(card: tuple[list[int], list[int]]):
    matches = len([e for e in card[1] if e in card[0]])
    return matches

def puzz01(puzz):
    total = 0
    for card in puzz.values():
        s = score(card)
        if s > 0:
            total += 2 ** (s-1)
    return total

def puzz02(puzz):
    card_amts = {}
    for id_ in puzz.keys():
        card_amts[id_] = 1
    for id_, card in sorted(puzz.items()):
        s = score(card)
        for idd in range(id_ + 1, id_ + s + 1):
            card_amts[idd] += card_amts[id_]
    return sum(card_amts.values())

samp = parse(sample)
print(puzz01(samp))
print(puzz02(samp))

with open('input04.dat', 'r') as f:
    puzzle = parse(f.read())

print(puzz01(puzzle))
print(puzz02(puzzle))
