with open('input01.dat') as file:
    data = file.read()

sample="91212129"

def part_one(data):
    numbas = [int(x) for x in data.strip()]
    return sum([x for i, x in enumerate(numbas) if (i < len(numbas) - 1 and x == numbas[i + 1]) or (i == len(numbas) - 1 and x == numbas[0])])

def part_two(data):
    numbas = [int(x) for x in data.strip()]
    return sum([x for i, x in enumerate(numbas) if (x == numbas[(i + len(numbas) // 2) % len(numbas)])])


print(part_one(data))
print(part_two(data))