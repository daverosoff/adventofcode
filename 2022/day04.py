sample="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def do_ranges_overlap(line: str, flag: bool=None) -> bool:
    left, right = line.split(',')
    x, y = map(int, left.split('-'))
    a, b = map(int, right.split('-'))
    l_set = set(range(x, y + 1))
    r_set = set(range(a, b + 1))
    if not flag:
        return l_set <= r_set or r_set <= l_set
    else:
        return bool(l_set.intersection(r_set))


def part_one(inp: str) -> int:
    trials = [do_ranges_overlap(line) for line in inp.splitlines()]
    return sum(trials)


def part_two(inp: str) -> int:
    trials = [do_ranges_overlap(line, True) for line in inp.splitlines()]
    return sum(trials)


with open('input04.dat') as f:
    puzzle = f.read()
print(f"part one: {part_one(puzzle)}")
print(f"part two: {part_two(puzzle)}")
