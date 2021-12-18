sample = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

# sample_two = """}}]])})]
# )}>]})
# }}>}>))))
# ]]}}]}]}>
# ])}>"""

lefts = "([{<"
rights = ")]}>"
matches = {lefts[i]: rights[i] for i in range(len(lefts))}
matches_two = {lefts[i]: i + 1 for i in range(len(lefts))}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

def first_illegal(line):
  stack = []
  for i, ch in enumerate(line):
    if ch in lefts:
      stack.append(ch)
    elif ch in rights:
      if stack:
        if ch != matches[stack[-1]]:
          # print(f"Error: expected {matches[stack[-1]]} but got {ch} instead")
          return points[ch]
        else:
          stack.pop()
      else:
        return points[ch]
  return 0

def part_one(data):
  result = 0
  for line in data:
    result += first_illegal(line)
  return result

def part_two(data):
  scores = []
  for line in data:
    if not first_illegal(line):
      stack = []
      for ch in line:
        if ch in lefts:
          stack.append(ch)
        elif ch in rights:
          stack.pop()
      new_score = 0
      while stack:
        new_score *= 5
        new_score += matches_two[stack.pop()]
      scores.append(new_score)
      print(f"Appending score {new_score}")
  return sorted(scores)[len(scores) // 2]

try:
  with open('input10.dat') as file:
    inp = file.read()
except FileNotFoundError:
  with open('2021/input10.dat') as file:
    inp = file.read()


print(part_one(inp.split('\n')))
print(part_two(inp.split('\n')))