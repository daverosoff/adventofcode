from math import prod

sample = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def get_naybs(arr, x, y):
    xmin = 0
    ymin = 0
    xmax = len(arr[0]) - 1
    ymax = len(arr) - 1
    poss = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    naybs = set([(i, j) for (i, j) in poss if (xmin <= i <= xmax) and (ymin <= j <= ymax)])
    return naybs

def is_min(arr, x, y):
    naybs = get_naybs(arr, x, y)
    return all([arr[y][x] < arr[j][i] for (i, j) in naybs])

def get_basin_size(arr, x, y):
    assert(arr[y][x] < 9)
    basin = set([(x, y)])
    naybs = get_naybs(arr, x, y)
    while not all([(x, y) in basin for (x, y) in naybs if arr[y][x] < 9]):
        for (x, y) in naybs:
            if arr[y][x] < 9:
                basin.add((x, y))
            # naybs = naybs.union(get_naybs(arr, x, y))
            for (i, j) in get_naybs(arr, x, y):
                if arr[y][x] < 9:
                    naybs.add((x, y))
    return len(basin)

def puzzle(data):
    arr = [[int(ch) for ch in row.strip()] for row in data.split('\n') if row]
    xmax = len(arr[0]) - 1
    ymax = len(arr) - 1

    mins = []
    part_one = 0
    for x in range(xmax + 1):
        for y in range(ymax + 1):
            if is_min(arr, x, y):
                part_one += (1 + arr[y][x])
                mins.append((x, y))
    basin_sizes = sorted([get_basin_size(arr, x, y) for (x, y) in mins], reverse=True)
    part_two = prod(basin_sizes[:3])
    return part_one, part_two



with open('input09.dat') as file:
    input = file.read()

print(puzzle(sample))