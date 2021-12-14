import itertools

puzzle = """..##.##.
#.#..###
##.#.#.#
#.#.##.#
###..#..
.#.#..##
#.##.###
#.#..##."""

sample = """.#.
..#
###"""

class Cubie:
    def __init__(self, x, y, z, w, state):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.state = state
        self.next_state = state

    def is_active(self):
        return self.state == "#"

    def evolve(self):
        self.state = self.next_state

    def neighbors(self):
        xs = range(self.x - 1, self.x + 2)
        ys = range(self.y - 1, self.y + 2)
        zs = range(self.z - 1, self.z + 2)
        ws = range(self.w - 1, self.w + 2)
        return [n for n in itertools.product(xs, ys, zs, ws)
            if n != (self.x, self.y, self.z, self.w)]

class Grid:
    def __init__(self, st):
        st = st.split("\n")
        self.cubies = {}
        for i, x in enumerate(st): # row
            for j, y in enumerate(st): # column
                self.cubies[(i,j,0,0)] = Cubie(i, j, 0, 0, st[i][j])

    def __str__(self):
        xmin = min([n[0] for n in self.cubies])
        xmax = max([n[0] for n in self.cubies])
        ymin = min([n[1] for n in self.cubies])
        ymax = max([n[1] for n in self.cubies])
        zmin = min([n[2] for n in self.cubies])
        zmax = max([n[2] for n in self.cubies])
        wmin = min([n[2] for n in self.cubies])
        wmax = max([n[2] for n in self.cubies])

        planes = ""
        for w in range(wmin, wmax + 1):
            hyperplane = ""
            for z in range(zmin, zmax + 1):
                plane = ""
                for x in range(xmin, xmax + 1):
                    row = ""
                    for y in range(ymin, ymax + 1):
                        row += self.cubies[(x,y,z)].state
                    plane += row + "\n"
                planes += plane + "\n"
            hyperplanes += plane + "\n"
        return hyperplanes

    def evolve(self):
        for cubie in self.cubies.copy():
            neighbors = self.cubies[cubie].neighbors()
            for n in neighbors:
                if n not in self.cubies:
                    self.cubies[n] = Cubie(*n, '.')
        for cubie in self.cubies:
            neighbors = self.cubies[cubie].neighbors()
            num_active = len([n for n in neighbors if n in self.cubies and self.cubies[n].is_active()])
            if self.cubies[cubie].is_active():
                if num_active not in (2, 3):
                    self.cubies[cubie].next_state = '.'
            else:
                if num_active == 3:
                    self.cubies[cubie].next_state = '#'
        for cubie in self.cubies:
            self.cubies[cubie].evolve()

    def num_active(self):
        return len([cubie for cubie in self.cubies if self.cubies[cubie].is_active()])

g = Grid(puzzle)
for _ in range(6):
    g.evolve()
print(g.num_active())