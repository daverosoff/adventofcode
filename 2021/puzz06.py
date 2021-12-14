from collections import defaultdict

with open("input06.dat", 'r') as file:
    data = file.read()

sample = """3,4,3,1,2"""

class FishDict:
    def __init__(self, data):
        values = set(data)
        self.di = defaultdict(lambda: 0, {val: data.count(val) for val in values})
        # return di

    def __next__(self):
        self.di.update({
            0: self.di[1],
            1: self.di[2],
            2: self.di[3],
            3: self.di[4],
            4: self.di[5],
            5: self.di[6],
            6: self.di[0] + self.di[7],
            7: self.di[8],
            8: self.di[0]
        })
        # return fish_dict

def puzzle(input, part):
    time = 256 if part == 2 else 80
    fish = FishDict([int(x.strip()) for x in input.split(',')])
    for _ in range(time):
        next(fish)
        # fish = advance(fish)
    return sum(fish.di.values())

print(puzzle(data, 1))
print(puzzle(data, 2))