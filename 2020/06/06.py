
with open("input", 'r') as f:
  questions = f.read()

groups = questions.split("\n\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"

def unified():
  part_one, part_two = 0, 0
  for g in groups:
    union = set(g).intersection(alphabet)
    people = [person for person in g.split('\n') if person]
    intersection = [x for x in alphabet if all([(x in person) for person in people])]
    # intersection = set.intersection({set(person).intersection(alphabet) for person in g.split('\n')})
    part_one += len(union)
    part_two += len(intersection)
  print(f"Part one: {part_one}, part two: {part_two}")

unified()

# def part_one():
#   result = 0
#   for g in groups:
#     answers = [x for x in set(g) if x in alphabet]
#     result += len(answers)
#   return result

# print(f"Part one: {part_one()}");

# def part_two():
#   result = 0
#   for g in groups:
#     people = [set(x) for x in g.split("\n") if set(x)]
#     for person in people:
#       person = person.intersection(alphabet)
#     uniq = len(set.intersection(*people))
#     print(uniq)
#     result += uniq
#   return result

# print(f"Part two: {part_two()}")
