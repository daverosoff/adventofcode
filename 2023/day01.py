import numpy as np

sample = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

sample2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

with open("input01.dat", 'r') as f:
    puzzle = f.read()

lines = puzzle.split('\n')

def fix_first_word(line: str, last: bool = False) -> str:
    words = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten"]
    if last:
        words = [w[::-1] for w in words]
        line = line[::-1]
    idxs = [line.find(word) for word in words]
    idxs = [idx if idx != -1 else np.inf for idx in idxs]
    first_word = np.argmin(idxs)
    fixed = line.replace(words[first_word], str(first_word + 1), 1)
    if last:
        return fixed[::-1]
    return fixed

def get_cal(line: str):
    line_nums = "".join([ch for ch in line if ch.isnumeric()])
    return int("".join([line_nums[0], line_nums[-1]]))

def get_first(line: str) -> str:
    line_nums = "".join([ch for ch in line if ch.isnumeric()])
    return line_nums[0]

def get_last(line: str) -> str:
    line_nums = "".join([ch for ch in line if ch.isnumeric()])
    return line_nums[-1]

def puzz01(lines):
    x = []
    for line in lines:
        if line:
            x.append(get_cal(line))
    return sum(x)

def puzz02(lines):
    x = 0
    for line in lines:
        if line:
            y = get_first(fix_first_word(line))
            y += get_last(fix_first_word(line, True))
            x += int(y)
    return x

# print(puzz01(sample.split('\n')))
# print(puzz02(sample2.split('\n')))
print(puzz01(lines))
print(puzz02(lines))