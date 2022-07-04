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

class SegMapping:
    def __init__(self, st):
        self.string = "".join(sorted(st))
        self.set = set(self.string)

    def __eq__(self, other):
        return self.set == other.set

    def __le__(self, other):
        return self.set <= other.set

    def __lt__(self, other):
        return self.set < other.set

    def shared(self, other):
        return self.set.intersection(other.set)

segs = {
    0: SegMapping("abcefg"),
    1: SegMapping("cf"),
    2: SegMapping("acdeg"),
    3: SegMapping("acdfg"),
    4: SegMapping("bcdf"),
    5: SegMapping("abdfg"),
    6: SegMapping("abdefg"),
    7: SegMapping("acf"),
    8: SegMapping("abcdefg"),
    9: SegMapping("abcdfg")
}

def part_one(input):
    result = 0
    for row in input.split('\n'):
        _, rhs = row.split(" | ")
        for expr in rhs.split():
            if len(expr) in (2, 3, 4, 7):
                result += 1
    return result

def part_two_helper(words):
    lhs, rhs = words.split(" | ")
    our_segs = {}
    for word in lhs.split():
        ell = len(word)
        if ell not in our_segs.keys():
            our_segs[ell] = set()
            our_segs[ell].add(SegMapping(word).string)
        elif word not in our_segs[ell]:
            our_segs[ell].add(SegMapping(word).string)
    return our_segs

def part_two(input):
    our_segs = {}
    for line in input.split('\n'):
        our_segs.update(part_two_helper(line))
    code_book = {}
    # identify 1, 4, 7
    code_book.update({1: next(iter(our_segs[2]))})
    code_book.update({4: next(iter(our_segs[4]))})
    code_book.update({7: next(iter(our_segs[3]))})
    # identify 2, 3, 5
    # only 3 has all of a c f (from 7)
    code_book.update({3: [x for x in our_segs[5] if all([y in x for y in code_book[7]])][0]})
    our_segs[5].remove(code_book[3])
    two = [x for x in our_segs[5] if len(x.shared(code_book[4])) == 2]
    five = [x for x in our_segs[5] if len(x.shared(code_book[4])) == 3]
    print(code_book)

if __name__ == "__main__":
    with open('input08.dat') as file:
        data = file.read()

    print(part_one(data))
    part_two(data)