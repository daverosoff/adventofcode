from collections import defaultdict as dd

def part_one(inp):
    dic = dd(lambda: '.')
    for line in inp.splitlines():
        points = line.split(" -> ")
        assert(isinstance(points, tuple[tuple[int, int], tuple[int, int]]))
        while len(points) > 1:
            xh, yh = points[-2]
            xt, yt = points[-1]
            xrange = range(xh, xt + 1)
            yrange = range(yh, yt + 1)
            assert(len(xrange) == 1 or len(yrange) == 1)
            match xrange, yrange:
                case 1, _:
                    for y in yrange:
                        dic[(xh, y)] = '#'
                case _, 1:
                    for x in xrange:
                        dic[(x, yh)] = '#'
            points = points[:-2]

def fall(x, y, map):
    if map[(x, y)] == '#':
        return
    if map[(x, y + 1)] == '.':
        fall(x, y + 1, map)
        map[(x, y)] = '|'
    else:
        map[(x, y)] = '|'
        if map[(x - 1, y)] == '.':
            fall(x - 1, y, map)
        if map[(x + 1, y)] == '.':
            fall(x + 1, y, map)

