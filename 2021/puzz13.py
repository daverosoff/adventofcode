sample = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

with open("input13.dat", 'r') as f:
    puzz13 = f.read()

dots = set()
folds = []
for line in puzz13.split("\n")[:-1]:
    if line and line[:4] != "fold":
        x, y = line.split(',')
        dots.add((int(x), int(y)))
    elif line:
        _, _, z = line.split(' ')
        folds.append(z)
for inst in folds:
    fold_location = int(inst.split('=')[1])
    if inst[0] == 'x':
        for dot in dots.copy():
            if dot[0] > fold_location:
                dots.add((2 * fold_location - dot[0], dot[1]))
                dots.remove(dot)
    elif inst[0] == 'y':
        for dot in dots.copy():
            if dot[1] > fold_location:
                dots.add((dot[0], 2 * fold_location - dot[1]))
                dots.remove(dot)
print(len(dots))

def visualize(d):
    dots_f = sorted([(y, x) for (x, y) in d])
    row_max = max([row for (row, col) in dots_f])
    col_max = max([col for (row, col) in dots_f])
    for row in range(row_max + 1):
        row_st = ""
        for col in range(col_max + 1):
            row_st += ('#' if (row, col) in dots_f else ' ')
            # if (row, col) in dots_f:
            #     row_st += '#'
            # else:
            #     row_st += ' '
        print(row_st)

visualize(dots)
#for dot in dots:
#    print(dot)
#print(folds)