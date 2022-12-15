from collections import defaultdict as dd

sample = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

def find_bottom(inp):
    miny = min(int(line.split(" -> ")[0].split(",")[1]) for line in inp.splitlines())
    maxy = max(int(line.split(" -> ")[-1].split(",")[1]) for line in inp.splitlines())
    return miny, maxy

def fall(x, y, map, maxy):
    if y + 1 > maxy:
        return True
    elif map[(x, y + 1)] == '.':
        return fall(x, y + 1, map, maxy)
        # map[(x, y)] = '|'
    # elif map[(x, y + 1)] == '#':
    #     map[(x, y)] = 'o'
    #     return
    elif map[(x - 1, y + 1)] == '.':
            return fall(x - 1, y + 1, map, maxy)
    elif map[(x + 1, y + 1)] == '.':
            return fall(x + 1, y + 1, map, maxy)
    else:
        map[(x, y)] = 'o'
        return

def draw(map):
    minx = min(x for x, _ in map.keys())
    maxx = max(x for x, _ in map.keys())
    miny = min(y for _, y in map.keys())
    maxy = max(y for _, y in map.keys())
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(map[(x, y)], end='')
        print()

def part_one(inp):
    dic = dd(lambda: '.')
    miny, maxy = find_bottom(inp)
    for line in inp.splitlines():
        points = line.split(" -> ")
        while len(points) > 1:
            xh, yh = map(int, points[-2].split(','))
            xt, yt = map(int, points[-1].split(','))
            if xh > xt:
                xh, xt = xt, xh
            if yh > yt:
                yh, yt = yt, yh
            xrange = range(xh, xt + 1)
            yrange = range(yh, yt + 1)
            # assert(len(xrange) == 1 or len(yrange) == 1)
            match len(xrange), len(yrange):
                case _, 1:
                    for x in xrange:
                        dic[(x, yh)] = '#'
                case 1, _:
                    for y in yrange:
                        dic[(xh, y)] = '#'
            points = points[:-1]
    draw(dic)
    i = 0
    while True:
        if fall(500, 0, dic, maxy):
            draw(dic)
            print(f"Success! {i}")
            break
        i += 1
        # draw(dic)
        # print()

with open('input14.dat') as f:
    puzzle = f.read()

part_one(puzzle)


