sample = """A Y
B X
C Z"""


def parse_input(inp: str) -> list[tuple[str, str]]:
    result = []
    for line in inp.splitlines():
        if line:
            result.append((line[0], line[2]))
    return result


def score_one(a, x):
    match a, x:
        case ('A', 'X') | ('B', 'Y') | ('C', 'Z'):
            result = 3
        case ('A', 'Y') | ('B', 'Z') | ('C', 'X'):
            result = 6
        case ('A', 'Z') | ('B', 'X') | ('C', 'Y'):
            result = 0
        case _:
            raise ValueError("wtf")
    match x:
        case 'X':
            result += 1
        case 'Y':
            result += 2
        case 'Z':
            result += 3
        case _:
            raise ValueError("wtf??")
    return result


def score_two(a, x):
    match a, x:
        case ('A', 'X') | ('B', 'X') | ('C', 'X'):
            result = 0
        case ('A', 'Y') | ('B', 'Y') | ('C', 'Y'):
            result = 3
        case ('A', 'Z') | ('B', 'Z') | ('C', 'Z'):
            result = 6
        case _:
            raise ValueError("wtf")
    match a, x:
        case ('B', 'X') | ('A', 'Y') | ('C', 'Z'):
            result += 1
        case ('B', 'Y') | ('A', 'Z') | ('C', 'X'):
            result += 2
        case ('B', 'Z') | ('A', 'X') | ('C', 'Y'):
            result += 3
        case _:
            raise ValueError("wtf??")
    return result


with open("input02.dat") as f:
    puzzle = f.read()


print(f"part one: {sum([score_one(a, x) for a, x in parse_input(puzzle)])}")
print(f"part two: {sum([score_two(a, x) for a, x in parse_input(puzzle)])}")