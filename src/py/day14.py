from pathlib import Path
import re
import math

num_re = re.compile(r'-?\d+')

with ((Path(__file__).parent.parent.parent) / "data" / "14.in").open() as f:
    robots = [[int(x) for x in num_re.findall(line)] for line in f.read().strip().splitlines()]

T = 100
W = 101
H = 103

def print_robots():
    grid = [['.' for j in range(W)] for i in range(H)]
    for px, py, *_ in robots:
        grid[py][px] = '#'
    print('\n'.join(''.join(line) for line in grid))

# t = 0
best_deviation = len(robots) * math.sqrt(W * W + H * H)
p2 = 0
for t in range(1, 10001):
    meanx = 0
    meany = 0
    for robot in robots:
        px, py, vx, vy = robot
        robot[0] = px = (px + vx) % W
        robot[1] = py = (py + vy) % H
        meanx += py
        meany += py
    # t += 1
    meanx /= len(robots)
    meany /= len(robots)
    deviation = sum(math.sqrt((px - meanx)**2 + (py - meany)**2) for px, py, *_ in robots)
    if deviation < best_deviation:
        best_deviation = deviation
        p2 = t
        print(f'{t=} {deviation=}')
        print_robots()
        print()
    # print(f'{t=}', end='\r')
    if t == T:
        mw = (W - 1) / 2
        mh = (H - 1) / 2
        factors = [0, 0, 0, 0]
        for px, py, *_ in robots:
            if px == mw or py == mh:
                continue
            i = 2 * (px > mw) + (py > mh)
            factors[i] += 1
        p1 = math.prod(factors)
        print(p1)

print(p2)
