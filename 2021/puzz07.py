sample = """16,1,2,0,4,2,7,1,2,14"""

def tri(n, part):
    return (n * (n + 1)) // 2 if part == 2 else n

def puzzle(data, part):
    lst = [int(x) for x in data.split(',')]
    a = min(lst)
    b = max(lst)
    return min([sum([tri(abs(y - x), part) for y in lst]) for x in range(a, b + 1)])

with open('input07.dat', 'r') as file:
    puzz = file.read()

print(puzzle(puzz, 1))
print(puzzle(puzz, 2))