with open("input02.dat", 'r') as file:
    lines = [line[:-1] for line in file.readlines()]


def part_one():
    x = 0
    y = 0
    for line in lines:
        direction, length = line.split(' ')
        length = int(length)
        if direction == 'forward':
            x += length
        elif direction == 'up':
            y -= length
        elif direction == 'down':
            y += length
        else:
            raise ValueError(f"error: {direction} not valid direction")

    part_one = x * y
    return part_one

def part_two():
    x = 0
    y = 0
    aim = 0
    for line in lines:
        direction, length = line.split(' ')
        length = int(length)
        if direction == 'down':
            aim += length
        elif direction == 'up':
            aim -= length
        else:
            x += length
            y += aim * length
    return x * y

print(f"part one: {part_one()}")
print(f"part two: {part_two()}")