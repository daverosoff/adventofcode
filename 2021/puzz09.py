import random
from collections import deque

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
    def is_valid(i, j):
        return xmin <= i <= xmax and ymin <= j <= ymax
    def naybs(x, y):
        poss = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        check = [(i, j) for (i, j) in poss if is_valid(i, j)]
        return check
    def pos_is_min(x, y):
        return all([arr[y][x] < arr[j][i] for (i, j) in naybs(x, y)])
    if part == 1:
        part_one_result = 0
        mins = []
        for x in range(xmax + 1):
            for y in range(ymax + 1):
                if pos_is_min(x, y):
                    part_one_result += (1 + arr[y][x])
                    mins.append((x, y))
        return part_one_result
    else:
        lookup_table = [(x, y) for x in range(xmax + 1)
                               for y in range(ymax + 1) if arr[y][x] < 9]
        def find_basin():
            x, y = lookup_table[0]
            count = 0
            def find_basin_helper(x, y):
                nonlocal count
                lookup_table.remove((x, y))
                # print(f"removing ({x}, {y})")
                count += 1
                # print(f"current basin is size {count}")
                for n in naybs(x, y):
                    if n in lookup_table:
                        find_basin_helper(*n)
                return count
            return find_basin_helper(x, y)
        basins = []
        while lookup_table:
            basins.append(find_basin())
        part_two_result = 1
        for b in sorted(basins, reverse=True)[:3]:
            part_two_result *= b
        return part_two_result

with open('2021/input09.dat') as file:
    input = file.read()

print(puzzle(input, 1))
print(puzzle(input, 2))