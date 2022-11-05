import numpy as np

sample = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

def build_risk_table(risks: str):
    lines = risks.split('\n')
    return np.array([int(ch) for row in lines for ch in row], int).reshape(len(lines) - 1, len(lines) - 1)

def get_max_risk(risks, cum_risks, i, j):
    risk = risks[i, j]
    if i == j == 0:
        return 0
    if 0 <= i - 1 < len(risks):
        left = cum_risks[i-1, j]
    else:
        return risk + cum_risks[i, j-1]
    if 0 <= j - 1 < len(risks[0]):
        up = cum_risks[i, j-1]
    else:
        return risk + cum_risks[i-1, j]
    risk += min(left, up)
    return risk

def populate(risks, cum_risks):
    ell = len(risks)
    for diag in range(2 * ell + 1):
        for row in range(diag + 1):
            col = diag - row
            if 0 <= row < ell and 0 <= col < ell:
                cum_risks[row, col] = get_max_risk(risks, cum_risks, row, col)
    return cum_risks

with open("input15.dat") as f:
    lines = f.read()

# puzzle = build_risk_table(lines)
risks = build_risk_table(lines)
cum_risks = np.zeros(risks.shape, int)
cum_risks = populate(risks, cum_risks)
print(cum_risks[-1, -1])
