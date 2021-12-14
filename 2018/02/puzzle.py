with open('input02.dat', 'r') as file:
    ids = [line for line in file.readlines()]

def has_n(st, n):
    freq_map = {}
    for ch in st:
        if ch not in freq_map:
            freq_map[ch] = 1
        else:
            freq_map[ch] += 1
    return any([v == n for v in freq_map.values()])

def has_two(st):
    return has_n(st, 2)

def has_three(st):
    return has_n(st, 3)

def part_one():
    pairs = 0
    triples = 0
    for id in ids:
        if has_two(id):
            pairs += 1
        if has_three(id):
            triples += 1
    return pairs * triples

print(part_one())

def get_match(st1, st2):
    count = 0
    first = None
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            count += 1
        if count == 1 and not first:
            first = i
        elif count > 1:
            return None
    return first if count == 1 else None

def part_two(ids=ids):
    for i, id in enumerate(ids):
        for j, other in enumerate(ids[i+1:]):
            m = get_match(id, other)
            if m is not None:
                print(i, j+i+1)
                return id[:m] + id[m+1:]

sample="""abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz""".split('\n')

print(part_two())