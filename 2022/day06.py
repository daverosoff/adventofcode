with open("input06.dat") as f:
    puzzle = f.read()

sample = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
sample2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
sample3 = "nppdvjthqldpwncqszvftbrmjlhg"
sample4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
sample5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def part_one(inp, flag=False):
    offset = 4 if not flag else 14
    for i in range(len(inp) - 3):
        if len(set(inp[i:i+offset])) == offset:
            return i + offset
    raise ValueError("wtf")


print(f"part one: {part_one(puzzle, True)}")
print(f"part one: {part_one(sample2)}")
print(f"part one: {part_one(sample3)}")
print(f"part one: {part_one(sample4)}")
print(f"part one: {part_one(sample5)}")
