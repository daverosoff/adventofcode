import re

sample = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

def expand(st, d, results):
    for ch in st:
        if ch in d:
            for var in d[ch]:
                if var != '|':
                    results.add(re.sub(ch, var, st))
            # [results.append(re.sub(var, rhs, st[:])) for rhs in d[var]]
    return results

rules_st, words = sample.split("\n\n")
rules_li = rules_st.split("\n")
words = words.split("\n")
rules = {}
for line in rules_li:
    # line = [(int(x), y) for x, y in line.split(": ")]
    x, y = line.split(": ")
    y = tuple([ch for ch in y if ch not in (' ', '\n')])
    line = [x, y]
    rules.update([line])

print(expand("0", rules, "0"))