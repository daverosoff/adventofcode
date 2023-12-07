sample ="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

class Puzzle:

    def __init__(self, puzz):
        self.seeds = []
        self.ss = {}
        self.sf = {}
        self.fw = {}
        self.wl = {}
        self.lt = {}
        self.th = {}
        self.hl = {}
        self.puzz = self.parse(puzz)

    def parse(self, puzz):
        lines = puzz.split('\n')
        active_map = None
        for line in lines:
            if not line:
                continue
            if line[:5] == 'seeds':
                self.seeds = [int(v) for v in line.split(': ')[1].split()]
            elif line[-4:] == 'map:':
                map_kind = line.split()[0].split('-')
                map_code = map_kind[0][0] + map_kind[2][0]
                match map_code:
                    case 'ss':
                        active_map = self.ss
                    case 'sf':
                        active_map = self.sf
                    case 'fw':
                        active_map = self.fw
                    case 'wl':
                        active_map = self.wl
                    case 'lt':
                        active_map = self.lt
                    case 'th':
                        active_map = self.th
                    case 'hl':
                        active_map = self.hl
                    case _:
                        raise ValueError(f"invalid map code: {map_code}")
            else:
                dest, source, length = [int(v) for v in line.split()]
                i = source
                j = dest
                n = 0
                while n < length:
                    active_map[i + n] = j + n
                    n +=1

    def get_seed_location(self, seed):
        soil = self.ss[seed] if seed in self.ss else seed
        fert = self.sf[soil] if soil in self.sf else soil
        water = self.fw[fert] if fert in self.fw else fert
        light = self.wl[water] if water in self.wl else water
        temp = self.lt[light] if light in self.lt else light
        hum = self.th[temp] if temp in self.th else temp
        loc = self.hl[hum] if hum in self.hl else hum
        return loc

    def part01(self):
        return min([self.get_seed_location(seed) for seed in self.seeds])

print(Puzzle(sample).part01())

with open('input05.dat', 'r') as f:
    puzz05 = f.read()

print(Puzzle(puzz05).part01())
