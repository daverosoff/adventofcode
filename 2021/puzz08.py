import code


sample = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

# class SegMapping:
#     def __init__(self, st):
#         self.string = "".join(sorted(st))
#         self.set = set(self.string)

#     def __eq__(self, other):
#         return self.set == other.set

#     def __le__(self, other):
#         return self.set <= other.set

#     def __lt__(self, other):
#         return self.set < other.set

#     def shared(self, other):
#         return self.set.intersection(other.set)

# segs = {
#     0: SegMapping("abcefg"),
#     1: SegMapping("cf"),
#     2: SegMapping("acdeg"),
#     3: SegMapping("acdfg"),
#     4: SegMapping("bcdf"),
#     5: SegMapping("abdfg"),
#     6: SegMapping("abdefg"),
#     7: SegMapping("acf"),
#     8: SegMapping("abcdefg"),
#     9: SegMapping("abcdfg")
# }



def part_one(input):
    result = 0
    for row in input.split('\n'):
        _, rhs = row.split(" | ")
        for expr in rhs.split():
            if len(expr) in (2, 3, 4, 7):
                result += 1
    return result

def decode(line):
    lhs, rhs = line.split(" | ")
    digits = lhs.split(" ")
    crypt = rhs.split(" ")
    key = {}
    for i in range(10):
        key[i] = None
    for digit in digits:
        if len(digit) == 2:
            key[1] = set([ch for ch in digit])
        elif len(digit) == 3:
            key[7] = set([ch for ch in digit])
        elif len(digit) == 4:
            key[4] = set([ch for ch in digit])
        elif len(digit) == 7: # len == 7, so 8
            key[8] = set([ch for ch in digit])
    # assert(all([key[x] for x in (1, 4, 7, 8)]) and
    #     all([not key[x] for x in (0, 2, 3, 5, 6, 9)]))
    fives = [set([ch for ch in digit]) for digit in digits if len(digit) == 5]
    sixes = [set([ch for ch in digit]) for digit in digits if len(digit) == 6]
    for poss_3 in fives:
        if key[7] <= poss_3:
            key[3] = poss_3
            break
    for poss_6 in sixes:
        if not key[7] <= poss_6:
            key[6] = poss_6
            break
    for poss_9 in sixes:
        if key[4] <= poss_9:
            key[9] = poss_9
            break
    for poss_0 in sixes:
        if key[6] != poss_0 and key[9] != poss_0:
            key[0] = poss_0
            break
    for poss_5 in fives:
        if key[3] != poss_5 and poss_5 <= key[6]:
            key[5] = poss_5
            break
    for poss_2 in fives:
        if key[3] != poss_2 and key[5] != poss_2:
            key[2] = poss_2
            break

    crypt = [set([ch for ch in cr]) for cr in crypt]
    result = 0
    for ch in crypt:
        for i in range(10):
            if key[i] == ch:
                # print(f"Decoded {ch} as {i}")
                result = 10 * result + i
                break
    return result

def part_two(input):
    lines = input.split("\n")
    values = [decode(line) for line in lines]
    return sum(values)

if __name__ == "__main__":
    with open('input08.dat') as file:
        data = file.read()
    # data = sample
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")