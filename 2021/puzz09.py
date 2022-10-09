sample = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def puzzle(data, part):
    # def find_basin
    arr = [[int(ch) for ch in row.strip()] for row in data.split('\n') if row]
    xmin = 0
    ymin = 0
    xmax = len(arr[0]) - 1
    ymax = len(arr) - 1
    def pos_is_min(x, y):
        poss = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        check = [(i, j) for (i, j) in poss if xmin <= i <= xmax and ymin <= j <= ymax]
        return all([arr[y][x] < arr[j][i] for (i, j) in check])
    mins = []
    # if part == 1:
    part_one_result = 0
    for x in range(xmax + 1):
        for y in range(ymax + 1):
            if pos_is_min(x, y):
                part_one_result += (1 + arr[y][x])
                mins.append((x, y))
    # else:
    part_two_result = 1
    arr2 = [[9 if x == 9 else 0 for x in row] for row in arr]


    return result

with open('input09.dat') as file:
    input = file.read()

print(puzzle(input))