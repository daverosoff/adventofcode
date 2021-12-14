sample = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

import numpy
def cmp(a, b):
    return numpy.sign(b - a)

def puzzle(data, part):
    marks = {}
    for line in data.split('\n'):
        x1, y1, x2, y2 = [int(t) for item in line.split(' -> ')
                for t in item.split(',')]
        if x1 == x2 or y1 == y2 or part == 2:
            x, y, dx, dy = x1, y1, cmp(x1, x2), cmp(y1, y2)
            while (cmp(x, x2) * cmp(x1, x2) != -1
                    and cmp(y, y2) * cmp(y1, y2) != -1):
                marks[(x, y)] = marks.setdefault((x, y), 0) + 1
                x += dx
                y += dy
    return len([x for x in marks if marks[x] > 1])

with open("input05.dat", 'r') as file:
    data = file.read()

print(puzzle(data, 1))
print(puzzle(data, 2))
