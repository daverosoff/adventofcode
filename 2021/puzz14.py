sample = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

with open("input14.dat", 'r') as f:
    puzz14 = f.read()

lines = puzz14.split('\n')
start = lines[0]
rules = {}
chars = set()
for line in lines[2:-1]:
    pair, insert = line.split(' -> ')
    rules[pair] = insert
for lhs, rhs in rules.items():
    chars.add(lhs[0])
    chars.add(lhs[1])
    chars.add(rhs)
def update_counts(counts):
    counts_delta = {key: 0 for key in rules}
    for p in counts:
        inter = rules[p]
        left = p[0] + inter
        right = inter + p[1]
        # counts_p = counts[p]
        counts_delta[left] += counts[p]
        counts_delta[right] += counts[p]
        counts_delta[p] -= counts[p]
    for p in counts:
        counts[p] += counts_delta[p]
    return counts

def pair_insert(st):
    st = list(st)
    ref = st[:]
    subs = []
    for i, a in enumerate(ref):
        if i < len(ref) - 1:
            b = st[i + 1]
            subs.append((i, a, rules[a+b], b))
    count = 0
    for sub in subs:
        st[sub[0] + count : sub[0] + count + 2] = sub[1] + sub[2] + sub[3]
        count += 1
    return "".join(st)

def part_one(st):
    for _ in range(10):
        st = pair_insert(st)
    counts = [(ch, st.count(ch)) for ch in chars]
    counts_ascending = sorted(counts, key=lambda x: x[1])
    min_, max_ = counts_ascending[0], counts_ascending[-1]
    return max_[1] - min_[1]

def part_two(counts):
    counts = {key: 0 for key in rules}
    for i in range(len(start) - 1):
        pair = start[i] + start[i+1]
        counts[pair] += 1
    for _ in range(40):
        counts = update_counts(counts)
    char_counts = {ch: 0 for ch in chars}
    for pair in counts:
        a, b = pair
        char_counts[a] += counts[pair]
        char_counts[b] += counts[pair]
    char_counts[start[0]] += 1
    char_counts[start[-1]] += 1
    divided = [(ch, char_counts[ch] // 2) for ch in char_counts]
    counts_ascending = sorted(divided, key=lambda x: x[1])
    min_, max_ = counts_ascending[0], counts_ascending[-1]
    return (max_[1] - min_[1])

print(part_one(start))
print(part_two(start))

