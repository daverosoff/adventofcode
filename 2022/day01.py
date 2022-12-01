sample = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

with open("input01.dat") as f:
    puzzle = f.read()


def part_one(inp, n=1):
    paragraphs = inp.split("\n\n")
    elf_items = [[int(p) for p in para.splitlines()] for para in paragraphs]
    sums = [sum(li) for li in elf_items]
    return sum(sorted(sums, reverse=True)[:n])


def part_two(inp):
    return part_one(inp, 3)


print(part_one(puzzle))
print(part_two(puzzle))