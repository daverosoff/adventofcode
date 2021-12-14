with open('input01.dat', 'r') as file:
    lines = [int(line) for line in file.readlines()]

def part_two():
    freq = 0
    seen = {freq}
    while True:
        for f in lines:
            freq += f
            if freq not in seen:
                seen.add(freq)
            else:
                return freq

print(part_two())
