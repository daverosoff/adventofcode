import string

sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def get_priority(item: str) -> int:
    if item in string.ascii_lowercase:
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def left_half(items: str) -> set[str]:
    ell = len(items)
    return set(items[ :ell//2])

def right_half(items: str) -> set[str]:
    ell = len(items)
    return set(items[ell//2: ])

def find_match(items: str) -> str:
    left, right = left_half(items), right_half(items)
    (match,) = left.intersection(right)
    return match

def part_one(inp: str) -> int:
    return sum([get_priority(find_match(line)) for line in inp.splitlines()])

def part_two(inp: str) -> int:
    result = 0
    for i in range(0, len(groups := inp.splitlines()), 3):
        group = groups[i:i+3]
        a, b, c = [set(elf) for elf in group]
        (match,) = a.intersection(b).intersection(c)
        result += get_priority(match)
    return result

with open("input03.dat") as f:
    puzzle = f.read()

print(f"part one: {part_one(puzzle)}")
print(f"part two: {part_two(puzzle)}")
