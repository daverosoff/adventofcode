sample1 = """5 1 9 5
7 5 3
2 4 6 8"""

sample2="""5 9 2 8
9 4 7 3
3 8 6 5"""

with open('input02.dat') as file:
    data = file.read()

def puzzle(data, part):
    rows = [[int(x.strip()) for x in row.split() if x.strip()] for row in data.split('\n')]
    if part != 2:
        return sum([max(row) - min(row) for row in rows])
    else:
        return sum([x // y for row in rows for x in row for y in row if x != y and x % y == 0])

print(puzzle(sample2, 2))
print(puzzle(data, 1))
print(puzzle(data, 2))