with open("input01.dat", 'r') as file:
    lines = [int(line[:-1]) for line in file.readlines()]

part_one = len([i for i in range(len(lines) - 1) if lines[i+1] > lines[i]])
part_two = len([i for i in range(len(lines) - 3) if sum(lines[i+1:i+4]) > sum(lines[i:i+3])])

print(f"Part one: {part_one}")
print(f"Part two: {part_two}")
