import math
from collections import defaultdict

def get_dist(n):
    n -= 1
    m = math.floor(math.sqrt(n))
    k = math.ceil(m/2)
    n = abs(n - 4*k**2)
    l = 3 if n > m else 1
    return k + abs(n-l*k)

class Spiral:
    def __init__(self, target, n, nextval=lambda t: t + 1):
        self.target = target
        self.n = n
        self.x, self.y = 0, 0
        self.dx, self.dy = 1, 2
        self.values = defaultdict(lambda: 0, {(self.x, self.y): n})
        self.nextval = nextval

    def __call__(self):
        while self.n < self.target:
            self.n = self.nextval(self.n)
            for _ in range(dx):
                self.x += 1 * sign(self.dx)
            self.values[(self.x, self.y)] = self.n
            self.dx = -1 * self.dx - 2
            self.n = self.nextval(self.n)
            for _ in range(dy):
                self.y += 1 * sign(self.dy)
            self.values[(self.x, self.y)] = self.n
            self.dy = -1 * self.dy - 2
            self.n = self.nextval(self.n)
            for _ in range(dx):
                self.x += 1 * sign(self.dx)
            self.values[(self.x, self.y)] = self.n
            self.dx = -1 * self.dx + 2
            self.n = self.nextval(self.n)
            for _ in range(dy):
                self.y += 1 * sign(self.dy)
            self.values[(self.x, self.y)] = self.n
            self.dy = -1 * self.dy + 2
        x, y = [k for k, v in self.values.items() if v == self.target][0]
        return x, y

def part_one(n):
    s = Spiral(n, 0)
    x, y = s()
    print(x, y)

# print(get_dist(1024))
# print(get_dist(289326))
part_one(1024)