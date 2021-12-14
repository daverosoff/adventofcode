with open("input03.dat", 'r') as file:
    lines = [line[:-1] for line in file.readlines()]

sample="""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split('\n')

# sample = [int(n) for n in sample.split('\n')]

def oftener_bit(lst, pos):
    one = 0
    for value in lst:
        if value[pos] == '1':
            one += 1
    if one > len(lst) / 2:
        return '1'
    elif one < len(lst) / 2:
        return '0'
    else:
        return ''

def flip(ch):
    return '0' if ch == '1' else '1'

def to_bin(bstring):
    return int(bstring, 2)

def part_one(data):
    gamma = "".join([oftener_bit(data, i) for i in range(len(data[0]))])
    eps = "".join([flip(ch) for ch in gamma])
    return to_bin(gamma) * to_bin(eps)

def part_two(data):
    main_bit = oftener_bit(data, 0)
    filtered = [line for line in data if line[0] == main_bit]
    for pos in range(1, len(lines[0])):
        ob = oftener_bit(filtered, pos)
        if ob:
            filtered = [line for line in filtered if line[pos] == ob]
        else:
            filtered = [line for line in filtered if line[pos] == '1']
        if len(filtered) == 1:
            oxygen = to_bin(filtered[0])
            break
    filtered = [line for line in data if line[0] != main_bit]
    for pos in range(1, len(lines[0])):
        ob = oftener_bit(filtered, pos)
        if ob:
            filtered = [line for line in filtered if line[pos] != ob]
        else:
            filtered = [line for line in filtered if line[pos] == '0']
        if len(filtered) == 1:
            co2 = to_bin(filtered[0])
            break
    return oxygen * co2

print(part_one(lines))
print(part_two(lines))


